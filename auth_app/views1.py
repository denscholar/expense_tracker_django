from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import UsernameValidationSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class UsernameValidationView(APIView):
    def post(self, request):
        serializer = UsernameValidationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username", "")
            if not username:
                response = {"error": "Username cannot be empty"}
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            
            elif username.isalnum():
                response = {
                    "username_valid": True,
                }
                return Response(data=response, status=status.HTTP_200_OK)
            
            elif User.objects.filter(username=username).exists():
                response = {
                    "error": "Username already exists",
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

            else:
                response = {
                    "error": "Username must only contain alphanumeric characters"
                }

                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "Invalid input data"}, status=status.HTTP_400_BAD_REQUEST
            )
