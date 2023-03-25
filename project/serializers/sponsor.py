from rest_framework import serializers


class SponsorSerializers(serializers.Serializer):
    from_email = serializers.EmailField(required=True)
    to_email = serializers.EmailField(required=True)
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    project = serializers.IntegerField(required=True)
