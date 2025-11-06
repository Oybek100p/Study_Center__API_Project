from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50, default='+998 xx xxx xx xx')
    classroom = models.ForeignKey(Classroom , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + self.last_name

# Create your models here.
