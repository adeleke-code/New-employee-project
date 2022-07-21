from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdmin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()
# Create your views here.


class UserListCreateView(APIView):

    # authentication_classes = [BasicAuthentication]
    # permission_classes = []


    def get(self, request, format=None):
        """Allows only admin users to get a list of all users
        """

        all_data = User.objects.filter(is_active=True)
        serializer = UserSerializer(all_data, many=True)

        data = {
            "message" : "success",
            "data_count": len(all_data),
            "data": serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="post", request_body=UserSerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        """API View to create new users"""

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()


            data = {
                "message":"success",
            }
            return Response(data, status=status.HTTP_201_CREATED)


        else:
            data = {
                "message":"failed",
                "error":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)