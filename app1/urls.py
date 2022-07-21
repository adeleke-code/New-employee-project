from django.urls import path
from . import views


urlpatterns = [
    path("employees/", views.EmployeeListView().as_view(), name="employee_list" ),
    path("branch/", views.BranchListView().as_view(), name="branch_list"),
    path("employees/<int:employee_id>/", views.EmployeeDetailView().as_view(), name="employee_detail" ),
    path("branch/<int:employee_id>/", views.BranchDetailView().as_view(), name="branch_detail" ),
]
