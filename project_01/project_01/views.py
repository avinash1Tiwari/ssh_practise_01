from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SSHUser
from .serializers import SSHUserSerializer


# CREATE + GET ALL
class SSHUserListCreateView(APIView):

    # Get all users
    def get(self, request):
        users = SSHUser.objects.all()
        serializer = SSHUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create new user
    def post(self, request):
        serializer = SSHUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET ONE + UPDATE + DELETE
class SSHUserDetailView(APIView):

    def get_object(self, pk):
        try:
            return SSHUser.objects.get(id=pk)
        except SSHUser.DoesNotExist:
            return None


    # Get single user
    def get(self, request, pk):
        user = self.get_object(pk)

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SSHUserSerializer(user)
        return Response(serializer.data)


    # Update user
    def put(self, request, pk):
        user = self.get_object(pk)

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SSHUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Updated successfully",
                    "data": serializer.data
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # Delete user
    def delete(self, request, pk):
        user = self.get_object(pk)

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        user.delete()

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )