from core.services.base_model_service import BaseModelService
from project.models import ProjectImage


class ProjectImageService(BaseModelService):
    model_class = ProjectImage
