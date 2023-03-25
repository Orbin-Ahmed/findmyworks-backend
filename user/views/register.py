from allauth.account.utils import complete_signup
from allauth.account.views import sensitive_post_parameters_m
from dj_rest_auth.app_settings import (
    TokenSerializer, create_token,
)
from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.utils import jwt_encode
from django.conf import settings
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from user.serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    token_model = TokenModel
    throttle_scope = 'dj_rest_auth'

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_response_data(self, user):
        return TokenSerializer(user.auth_token, context=self.get_serializer_context()).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            errors = serializer.errors
            message = ''
            for error in errors:
                message += f"{error} - {errors[error][0]} "
            return Response({"detail": message},  status=status.HTTP_400_BAD_REQUEST)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)
        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)
        return response

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.access_token, self.refresh_token = jwt_encode(user)
        elif not getattr(settings, 'REST_SESSION_LOGIN', False):
            # Session authentication isn't active either, so this has to be
            #  token authentication
            create_token(self.token_model, user, serializer)

        complete_signup(
            self.request._request, user,
            False,
            None,
        )
        return user
