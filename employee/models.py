from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"
class Employee(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    age = models.IntegerField(default=None)
    Salary = models.IntegerField(default=None)
    address = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.role.name}"
