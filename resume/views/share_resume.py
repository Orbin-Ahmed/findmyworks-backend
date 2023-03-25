from rest_framework import views, status
from rest_framework.response import Response

from resume.services.share_resume import ShareResumeService


class ShareResume(views.APIView):
    service_class = ShareResumeService()

    def post(self, request, *args, **kwargs):
        user_id = self.kwargs.get("user_id")
        resume, status_code = self.service_class.get_resume(user_id)
        return Response(resume, status=status_code)
