from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=20, choices=[('HR', 'HR'), ('Normal', 'Normal Employee')])

    def __str__(self):
        return f"{self.name} - {self.email} - {self.group}"
    

class EmployeeToken(models.Model):
    token = models.CharField(max_length=100)
    user = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.token}"    
    

class Attendance(models.Model):
    date = models.DateField() 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.employee.name} - {self.date}"  

        
@receiver(post_save, sender=Employee)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        # Generate a unique token
        token_value = str(int(time.time() * 1000))
        EmployeeToken.objects.create(user=instance, token=token_value)