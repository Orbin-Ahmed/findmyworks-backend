"""findmyworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from findmyworks import settings
from user.views import GoogleLogin, FacebookLogin, AuthLoginView, RegisterView, emailView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/login/", AuthLoginView.as_view(), name='rest_login'),
    path("auth/", include("dj_rest_auth.urls")),
    path(
        "auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # path("auth/registration/", RegisterView.as_view()),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("auth/facebook/", FacebookLogin.as_view(), name="facebook_login"),
    # path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(
        r"^verify-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("user/", include("user.urls")),
    path("resume/", include("resume.urls")),
    path("project/", include("project.urls")),
    path("quiz/", include("quiz.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("user/welcome/", emailView.welcome_email, name="Welcome Email"),

]
