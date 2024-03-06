from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from faker import Faker
from django.views import View
from rest_framework import status
from django.shortcuts import render
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse


class FakerAPI(APIView):

    def post(self, request):
        fake = Faker()
        num_employees = int(request.data.get('num_employees',100))
        employees = []
        for i in range(num_employees):
            employee = Employee(
                name = fake.name(),
                email = fake.email(),
                address = fake.address(),
                city = fake.city()
            )
            employees.append(employee)
            
        Employee.objects.bulk_create(employees)
        serializer = EmployeeSerializer(employees, many=True )
        return Response(data=serializer.data, status=200)

class CreateAPI(View):
    def get(self, request, format=None):
        template = get_template('employee_list.html')
        employees = Employee.objects.all()
        context = {'employees':employees}
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
        if pdf.err:
            return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    
   