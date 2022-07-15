from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
from .serializers import BranchSerializer
from .models import Employee
from .models import Branch
import random

@api_view(["GET", "POST"])
def employee(request):
    if request.method == "GET":
        all_data = Employee.objects.all()

        serializer = EmployeeSerializer(all_data, many=True)

        data = {
            "message" : "success",
            "data_count" : len(all_data),
            "data" : serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)


    elif request.method == "POST":
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



@api_view(["GET", "POST"])
def branch(request):
    if request.method == "GET":

        all_branchs = Branch.objects.all()
        
        serializer = BranchSerializer(all_branchs, many=True)

        data = {
            "message" : "success",
            "data_count" : len(all_branchs),
            "data" : serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = BranchSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["branch_id"] = "".join([str(random.choice(range(10))) for _ in range(4)])
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


