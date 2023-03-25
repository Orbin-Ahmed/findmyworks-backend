from rest_framework import status, views
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from quiz.filters import SkillQuizResultFilter
from quiz.models import SkillQuizResult
from quiz.serializers import (
    SkillQuizSerializer, SkillQuizSubmissionSerializer,
    SkillQuizResultSerializer, CertificateSerializer
    )
from quiz.services import SkillQuizService, SkillQuizResultService


class SkillQuestionAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    service_class = SkillQuizService()
    serializer_class = SkillQuizSerializer

    def get(self, request, *args, **kwargs):
        # Todo: handle try catch.
        skill = request.query_params.get("skill")
        if not skill:
            return Response({"detail": "skill is required!"}, status=status.HTTP_400_BAD_REQUEST)
        questions_no = request.query_params.get("qn", 10)
        questions = self.service_class.get_random_question(skill, questions_no)
        response = self.serializer_class(questions, many=True)
        return Response(response.data, status=status.HTTP_200_OK)


class SkillQuizSubmissionAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    service_class = SkillQuizService()
    serializer_class = SkillQuizSubmissionSerializer

    def post(self, request, *args, **kwargs):
        # Todo: handle try catch.
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        skill_id = kwargs.get("skill_id")
        result_status, percentage = self.service_class.calculate_results(validated_data, skill_id, request.user)
        return Response({"status": result_status, "result_percent": percentage}, status=status.HTTP_200_OK)


class SkillQuizResultAPIView(ListAPIView):
    queryset = SkillQuizResult.objects.all().order_by("-result_percent")
    permission_classes = [IsAuthenticated]
    service_class = SkillQuizResultService()
    serializer_class = SkillQuizResultSerializer
    filterset_class = SkillQuizResultFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class SkillQuizResultRankingAPIView(ListAPIView):
    queryset = SkillQuizResult.objects.filter(status="Pass").order_by("-result_percent")
    permission_classes = [IsAuthenticated]
    service_class = SkillQuizResultService()
    serializer_class = SkillQuizResultSerializer
    filterset_class = SkillQuizResultFilter

    def get_queryset(self):
        skill = self.request.query_params.get("skill")
        data = self.queryset.filter(skill_id=skill).all()
        return data


class CertificatesAPIView(ListAPIView):
    queryset = SkillQuizResult.objects.filter(status="Pass").order_by("-result_percent")
    service_class = SkillQuizResultService()
    serializer_class = CertificateSerializer
    filterset_class = SkillQuizResultFilter

    def get_queryset(self):
        skill = self.request.query_params.get("skill")
        user_id = self.request.query_params.get("user_id")
        data = self.queryset.filter(skill_id=skill, user_id=user_id).all()
        return data
