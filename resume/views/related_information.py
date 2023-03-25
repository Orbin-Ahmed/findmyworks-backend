from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.images import ImageFile
# from rest_framework.permissions import IsAuthenticated
from PIL import Image
from io import BytesIO
from resume.models import RelatedInformation
from resume.serializers import (
    OtherRelatedInformationSerializer,
    FinalizeRelatedInformationSerializer,
    RelatedInformationImageSerializer,
    RelatedInformationImageDetailSerializer,
)
from resume.services import RelatedInformationService, RelatedInformationImageService
from django.http import QueryDict

def convert_to_webp(image, aspect_ratio=None):
    # Open the image using Pillow
    im = Image.open(image)

    # Resize the image to the specified aspect ratio (if provided)
    if aspect_ratio:
        width, height = im.size
        new_height = int(width / aspect_ratio)
        if new_height > height:
            new_width = int(height * aspect_ratio)
            left = int((width - new_width) / 2)
            top = 0
            right = int(left + new_width)
            bottom = height
        else:
            left = 0
            top = int((height - new_height) / 2)
            right = width
            bottom = int(top + new_height)
        im = im.crop((left, top, right, bottom))

    # Create a BytesIO object to hold the image data in memory
    buffer = BytesIO()

    # Save the image in WebP format to the buffer
    im.save(buffer, "webp")

    # Seek to the start of the buffer so the data can be read
    buffer.seek(0)

    return buffer

class OtherRelatedInformationViewSet(viewsets.ModelViewSet):
    queryset = RelatedInformation.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = OtherRelatedInformationSerializer
    service_class = RelatedInformationService()
    http_method_names = ['get', 'post']
    pagination_class = None

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset().first())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        instance = self.get_queryset().first()
        if not instance:
            instance = self.service_class.create({"user": self.request.user})
        self.service_class.update(instance, validated_data, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FinalizeRelatedInformationViewSet(viewsets.ModelViewSet):
    queryset = RelatedInformation.objects.all()
    serializer_class = FinalizeRelatedInformationSerializer
    service_class = RelatedInformationService()
    http_method_names = ['get', 'post']
    pagination_class = None

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset().first())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        instance = self.get_queryset().first()
        if not instance:
            instance = self.service_class.create({"user": self.request.user})
        self.service_class.update(instance, validated_data, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RelatedInformationImageAPIView(APIView):
    serializer_class = RelatedInformationImageSerializer
    service_class = RelatedInformationImageService()

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        image = data["image"]
        webp_file = convert_to_webp(image)
        file_name = data["image"].name.split(".")[0]
        file_name = file_name + ".webp"
        image = ImageFile(BytesIO(webp_file.read()), name=file_name)
        print(type(image))
        data["image"] = image
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        instance = self.service_class.create(validated_data, **kwargs)
        response = RelatedInformationImageDetailSerializer(instance, context={"request": self.request})
        return Response(response.data, status=status.HTTP_200_OK)
