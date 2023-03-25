from core.services.base_model_service import BaseModelService
from resume.models import RelatedInformation, RelatedInformationImage
from resume.services import InstituteService


class RelatedInformationService(BaseModelService):
    model_class = RelatedInformation
    institute_service = InstituteService()

    def update(self, instance, validated_data, **kwargs):
        request = kwargs.get("request")
        user = self.core_service.get_user(request)
        validated_data["updated_by"] = user
        pre_publication = instance.publications if instance.publications else []
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if len(instance.publications) > len(pre_publication):
            self.institute_service.add_batch_publication(instance.user, True)
        elif len(instance.publications) < len(pre_publication):
            self.institute_service.add_batch_publication(instance.user, False)
        return instance


class RelatedInformationImageService(BaseModelService):
    model_class = RelatedInformationImage
