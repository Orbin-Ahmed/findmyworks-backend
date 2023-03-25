from core.services.base_model_service import BaseModelService
from project.models import ProjectActivity


class ProjectActivityService(BaseModelService):
    model_class = ProjectActivity
