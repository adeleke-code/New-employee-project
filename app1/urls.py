from django.urls import path
from . import views


urlpatterns = [
    path("employees/", views.employee, name="employee_list"),
    path("branch/", views.branch, name="branch_list")

]
