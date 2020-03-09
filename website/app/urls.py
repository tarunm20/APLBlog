from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>', views.post, name='post'),
    path('signup', views.signup, name='signup')
]
