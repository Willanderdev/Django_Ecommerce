
from .views import RegisterView, IndexView, UpdateUserView, UpdateePasswordview
from django.urls import path

from django.conf.urls.static import static


urlpatterns = [

    path('profile', IndexView.as_view(), name='profile'),
    path('register', RegisterView.as_view(), name='register'),
    path('update', UpdateUserView.as_view(), name='update'),
    path('alter_senha', UpdateePasswordview.as_view(), name='alter_senha'),

]
