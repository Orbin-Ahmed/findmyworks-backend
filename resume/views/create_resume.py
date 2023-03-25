from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from resume.serializers.create_resume import CreateResumeSerializer
from resume.services.create_resume import CreateResumeService


class CreateResumeAPIView(APIView):
    service_class = CreateResumeService()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateResumeSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        message, resume_status = self.service_class.create(user, validated_data, **kwargs)
        return Response({"detail": message}, status=resume_status)
