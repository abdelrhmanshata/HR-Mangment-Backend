from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Employee,EmployeeToken,Attendance

admin.site.register(Employee)
admin.site.register(EmployeeToken)

admin.site.register(Attendance)
