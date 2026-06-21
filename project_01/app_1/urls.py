from django.urls import path
from .views import UserView,HelloAPIView
from .views import SSHUserListCreateView, SSHUserDetailView


urlpatterns = [
      path('test', UserView.as_view()),
      path('hello', HelloAPIView.as_view()),
      path("users/", SSHUserListCreateView.as_view(), name="user-list-create"),
      path("users/<int:pk>/", SSHUserDetailView.as_view(), name="user-detail"),
]

