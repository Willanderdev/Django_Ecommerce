from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import messages


class ModelBackend(BaseModelBackend):
    
    def authenticate(self, request, username=None, password=None):
        if username != None:
            UserModel = get_user_model()
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
                else:
                    messages.error(
                        request, 'senha incorreta')
                    
            except User.DoesNotExist:
                pass
  
