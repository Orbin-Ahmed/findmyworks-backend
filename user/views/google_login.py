from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView, OAuth2CallbackView
from dj_rest_auth.registration.views import SocialLoginView

from findmyworks import settings


class GoogleLogin(SocialLoginView):     # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.CALLBACK_URL
    # callback_url = 'http://localhost:8000/account/google/login/callback/'


oauth2_login = OAuth2LoginView.adapter_view(GoogleOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(GoogleOAuth2Adapter)
