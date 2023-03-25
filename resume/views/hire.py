from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import send_general_email
from findmyworks import settings
from resume.serializers import HireSerializers
from user.services import UserService


class HireAPIViewSet(APIView):
    serializer_class = HireSerializers
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        site_name = "findmywork.com"
        subject_template_name = "hire/hire.txt"
        html_email_template_name = "hire/hire.html"
        default_email = settings.FROM_EMAIL
        extra_email_context = None
        email_user = self.user_service.all(email=validated_data.get("to_email")).first()
        if not email_user:
            return Response(
                {"detail": "User doesn't exits!"}, status=status.HTTP_400_BAD_REQUEST
            )
        context = {
            "subject": validated_data.get("subject"),
            "from_email": validated_data.get("from_email"),
            "to_email": validated_data.get("to_email"),
            "message": validated_data.get("message"),
            "site_name": site_name,
            "user_name": email_user.full_name,
            **(extra_email_context or {}),
        }
        send_general_email(
            subject_template_name,
            context,
            default_email,
            validated_data.get("to_email"),
            html_email_template_name,
        )
        return Response({"result_status": "Hire mail send!"}, status=status.HTTP_200_OK)
