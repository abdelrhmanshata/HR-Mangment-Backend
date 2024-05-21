from django.urls import path
from employees import views as views

urlpatterns = [
    # GET POST from rest framework class based view APIView
    path('employees/', views.Employee_List.as_view(),name='employee-list'),
    # GET PUT DELETE from rest framework class based view APIView
    path('employees/<int:pk>',views.Employee_PK.as_view(),name='employee-details'),  
    # POst from rest framework class based view APIView
    path('employee_attendances/',views.Employee_Attendance.as_view(),name='employee-details'),  
    # POST from rest framework class based view APIView  
    path('register/', views.RegisterView.as_view(), name='register'),
    # POST from rest framework class based view APIView
    path('login/', views.LoginView.as_view(), name='login'),
]
