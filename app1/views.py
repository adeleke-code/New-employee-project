from http.client import NOT_FOUND
from django.http import response
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import APIView, action
from .serializers import EmployeeSerializer
from .serializers import BranchSerializer
from .models import Employee
from .models import Branch
from rest_framework.views import APIView;
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
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


class EmployeeDetailView(APIView):

    def get_object(self, employee_id):
        try:
            return Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise NotFound(detail={"message":"Employee not found"}, code=status.HTTP_404_NOT_FOUND)


    def get(self, request, employee_id, format=None ):
        """Api view to get the details of an employee"""
        obj = self.get_object(employee_id)
        serializer = EmployeeSerializer(obj)
        data = {
            "message" : "success",
            "data": serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=EmployeeSerializer())
    @action(methods=["put"], detail=True)
    def put(self, request, employee_id, format=None):
        """API View to edit employees"""

        obj  =  self.get_object(employee_id)
        serializer = EmployeeSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            if "employee_num" in serializer.validated_data.keys():
                raise PermissionDenied(detail={"message":"you cannot edit your employee number"}, code=status.HTTP_403_FORBIDDEN)

            serializer.save()

            data = {
                "message":"success",
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)


        else:
            data = {
                "message":"failed",
                "error":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, employee_id, format=None):
        """Delete an employee"""

        obj  =  self.get_object(employee_id)
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class BranchDetailView(APIView):
    def get_object(self, branch_id):
        try:
            return Branch.objects.get(id=branch_id)
        except Branch.DoesNotExist:
            raise NotFound(detail={"message":"Branch not found"}, code=status.HTTP_404_NOT_FOUND)

    def get(self, request, branch_id, format=None):
        """API view to get the list of branches"""
        obj = self.get_object(branch_id)
        serializer = BranchSerializer(obj)
        data = {
            "message":"success",
            "data" : serializer.data
        }

        return Response(data, status-status.HTTP_200_OK)

    @swagger_auto_schema(method="put", request_body=BranchSerializer())
    @action(methods=["put"], detail=True)
    def put(self, request, employee_id, format=None):
        """"API view to edit branches"""
        obj = self.get_object(employee_id)
        serializer = BranchSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            if "branch_id" in serializer.validated_data.keys():
                raise PermissionDenied(detail={"message":"You can not edit your branch_id"}, code=status.HTTP_403_FORBIDDEN)
            
            serializer.save()
            data = {
                "message":"success"
  
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)

        else:
            data = {
                "message":"failed",
                "error":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, branch_id, format=None):
        """Delete a branch"""
        obj = self.get_object(branch_id)
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

