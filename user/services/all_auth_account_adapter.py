from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from findmyworks import settings


class CustomAllAuthAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url.

        Note that if you have architected your system such that email
        confirmations are sent outside of the request context `request`
        can be `None` here.
        """
        current_site = get_current_site(request)
        url = reverse("account_confirm_email", args=[emailconfirmation.key])
        # ret = build_absolute_uri(request, url)
        return f"{settings.API_PROTOCOL}://{current_site}{url}"
