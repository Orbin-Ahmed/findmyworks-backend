
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ResumeBaseViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    permission_classes = [IsAuthenticated]
    service_class = None
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        self.service_class.update_or_create_instance(validated_data, request.user, **kwargs)
        instances = self.service_class.all(user=self.request.user)
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)
