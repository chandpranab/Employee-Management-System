from django.test import TestCase
from .models import Employee, Role
from django.urls import reverse
# Create your tests here.

class Unittest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='TestRole')
        self.employee = Employee.objects.create(name="Testing", role=self.role, age=40, Salary=1000)

    def test_model_employee(self):
        cnt = Employee.objects.all().count()
        emp = Employee.objects.get(name='Testing')
        self.assertEqual(1, cnt)
        self.assertEqual(emp.name,'Testing')
        self.assertEqual(emp.age,40)
        self.assertEqual(emp.Salary,1000)

    def test_model_role(self):
        cnt = Role.objects.all().count()
        role = Role.objects.all()[0]
        self.assertEqual(1, cnt)
        self.assertEqual(role.name,'TestRole')

    def test_view_employee(self):
        response = self.client.get(reverse('emp_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'emp_list.html')

    def test_view_edit_employee(self):
        response = self.client.get(reverse('edit_emp', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'edit.html')

    def test_view_delete_employee(self):
        emp2 = Employee.objects.create(name="Testing2", role=self.role, age=40, Salary=1000)
        cnt = Employee.objects.all().count()
        self.assertEqual(cnt,2)
        response = self.client.get(reverse('delete_emp', kwargs={'pk':2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/employees/')
        cnt = Employee.objects.all().count()
        self.assertEqual(cnt,1)