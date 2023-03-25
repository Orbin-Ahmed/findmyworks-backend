from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from resume.serializers import UniversityRankingSerializer, CollegeRankingSerializer, SchoolRankingSerializer
from resume.services import RankingService


class UniversityRankingAPIView(APIView):
    serializer_class = UniversityRankingSerializer
    service_class = RankingService()

    def get(self, request, *args, **kwargs):
        queryset = self.service_class.get_university_ranking()
        response = self.serializer_class(queryset, many=True)
        return Response(response.data, status=status.HTTP_200_OK)


class CollegeRankingAPIView(APIView):
    serializer_class = CollegeRankingSerializer
    service_class = RankingService()

    def get(self, request, *args, **kwargs):
        queryset = self.service_class.get_college_ranking()
        response = self.serializer_class(queryset, many=True)
        return Response(response.data, status=status.HTTP_200_OK)


class SchoolRankingAPIView(APIView):
    serializer_class = SchoolRankingSerializer
    service_class = RankingService()

    def get(self, request, *args, **kwargs):
        queryset = self.service_class.get_school_ranking()
        response = self.serializer_class(queryset, many=True)
        return Response(response.data, status=status.HTTP_200_OK)
