from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import APIView, action
from .serializers import EmployeeSerializer
from .serializers import BranchSerializer
from .models import Employee
from .models import Branch
from rest_framework.views import APIView;
from drf_yasg.utils import swagger_auto_schema
import random

class EmployeeListView(APIView):

    def get(self, request, format=None):
        """"Allows the user to get a list of all employees
        """
        all_data = Employee.objects.all()
        serializer = EmployeeSerializer(all_data, many=True)
        data = {
            "message" : "success",
                "data_count" : len(all_data),
        "data" : serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method="post", request_body=EmployeeSerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        """API view to create new employees"""
        serializer = EmployeeSerializer(data=request.data)


        if serializer.is_valid():
            serializer.validated_data["employee_num"] = "".join([str(random.choice(range(10))) for _ in range(6)])
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



class BranchListView(APIView):

    def get(self, request, format=None):
        """"Allows the user to get a list of all employees
        """
        all_data = Branch.objects.all()
        serializer = BranchSerializer(all_data, many=True)
        data = {
            "message" : "success",
                "data_count" : len(all_data),
        "data" : serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="post", request_body=BranchSerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        """API view to create new Branch"""
        serializer = BranchSerializer(data=request.data)


        if serializer.is_valid():
            serializer.validated_data["branch_id"] = "".join([str(random.choice(range(10))) for _ in range(6)])
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