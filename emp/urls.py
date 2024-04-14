from django.urls import path
from . import views

urlpatterns = [
    path('', views.Employee.index, name='index'),
    path('create-employee', views.Employee.create_emp, name='create-employee'),
    path('edit-employee', views.Employee.edit_emp, name='edit-employee'),
    path('delete-employee', views.Employee.delete_emp, name='delete-employee'),
    path('update-employee', views.Employee.update_emp, name='update-employee'),
    
    path('search-employee', views.DB.search_employee, name='search-employee'),
    path('load-employee', views.DB.load_data, name='load-employee'),
    path('test-net', views.DB.test_net, name='test-net'),
    path('reset', views.DB.reset, name='reset'),
]
