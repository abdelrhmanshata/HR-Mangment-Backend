# employees/views.py
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Employee, EmployeeToken,Attendance
from .serializers import EmployeeSerializer

# CBV Class based views
# List and Create == GET and POST
class Employee_List(APIView):
    def get(self, request):
        employees = Employee.objects.filter(group="Normal")
        serializer = EmployeeSerializer(employees, many = True) 
        return Response(serializer.data)
    def post(self, request):
        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

#GET PUT DELETE cloass based views -- pk 
class  Employee_PK(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        if employee is None:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
        
    def put(self, request, pk):
        employee = self.get_object(pk)
        if employee is None:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        employee = self.get_object(pk)
        if employee is None:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class Employee_Attendance(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None
        
    def post(self, request, format=None):
        # Get the employee id and date from the request data
        employee_id = request.data.get('id')
        date = request.data.get('date')
        # Validate the input
        if not employee_id or not date:
            return Response({"error": "Employee ID and date are required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Retrieve the employee object
            employee = self.get_object(employee_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)

        obj = Attendance.objects.create(employee = employee , date=date);  
        obj.save()
        return Response({"Msg":"Done"}, status=status.HTTP_201_CREATED)
      
class RegisterView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
           {"errors":serializer.errors},
            status= status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')           
        try:
            user = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            user = None  
                              
        if user is not None : 
            if user.group == 'HR':
                my_token = EmployeeToken.objects.get(user=user)
                return Response({'token': my_token.token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Only HR employees can log in.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)
