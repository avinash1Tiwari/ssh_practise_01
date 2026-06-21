from rest_framework import serializers
from .models import SSHUser


class SSHUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSHUser
        fields = "__all__"