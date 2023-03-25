from allauth.account.models import EmailAddress
from dj_rest_auth.views import LoginView
from rest_framework import status
from rest_framework.response import Response


class AuthLoginView(LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework

    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        validated_data = self.serializer.validated_data
        is_verified = (
            EmailAddress.objects.filter(
                email=validated_data.get("email"), user=validated_data.get("user")
            )
            .first()
            .verified
        )
        if not is_verified:
            return Response({"detail": "Please, Verify your email first!"}, status=status.HTTP_400_BAD_REQUEST)
        self.login()
        return self.get_response()
