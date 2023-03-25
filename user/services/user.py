from core.services.base_model_service import BaseModelService
from user.models import User


class UserService(BaseModelService):
    model_class = User
