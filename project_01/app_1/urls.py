from django.urls import path
from .views import UserView,HelloAPIView

urlpatterns = [
      path('test', UserView.as_view()),
      path('hello', HelloAPIView.as_view()),
]

