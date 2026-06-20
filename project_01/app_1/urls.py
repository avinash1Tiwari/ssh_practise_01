from django.urls import path
from .views import UserView

urlpatterns = [
      path('test', UserView.as_view()),
]

