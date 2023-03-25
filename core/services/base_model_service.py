from rest_framework.generics import get_object_or_404

from core.services.core_service import CoreService


class BaseModelService:
    model_class = None

    def __init__(self):
        self.core_service = CoreService()

    def prepare_data(self, validated_data):
        return validated_data

    def get_model_class(self):
        assert self.model_class is not None, (
                "%s should include model_class attribute or override get_model_class() method"
                % self.__class__.__name__
        )
        return self.model_class

    def create(self, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)
        model_class = self.get_model_class()
        request = kwargs.get("request")
        user = self.core_service.get_user(request)
        validated_data["created_by"] = user
        validated_data["updated_by"] = user
        instance = model_class.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data, **kwargs):
        request = kwargs.get("request")
        user = self.core_service.get_user(request)
        validated_data["updated_by"] = user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def get(self, **kwargs):
        model_class = self.get_model_class()
        instance = get_object_or_404(model_class, **kwargs)
        return instance

    def update_status(self, instance, validated_data, **kwargs):
        instance.is_active = validated_data["is_active"]
        request = kwargs.get("request")
        user = self.core_service.get_user(request)
        validated_data["updated_by"] = user
        instance.save()
        return instance

    def all(self, **kwargs):
        model_class = self.get_model_class()
        instances = model_class.objects.filter(**kwargs)
        return instances

    def delete(self, **kwargs):
        instance = self.get_model_class().objects.filter(**kwargs)
        instance.delete()
        return True

    def update_or_create_instance(self, validated_data_list, user, **kwargs):
        for validated_data in validated_data_list:
            validated_data["user"] = user
            instance, _ = self.get_model_class().objects.update_or_create(
                id=validated_data.get("id"),
                defaults=validated_data
            )

    def get_or_create_instance(self, name):
        instance, _ = self.get_model_class().objects.get_or_create(name=name)
        return instance
