class CoreService:
    def get_user(self, request):
        if request and request.user.is_authenticated:
            return request.user
        return None
