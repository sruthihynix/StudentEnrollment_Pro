from django.db import models

# Create your models here.
class stud(models.Model):
    s_name=models.CharField(max_length=100)
    s_class=models.CharField(max_length=100)
    s_addr = models.CharField(max_length=100)
    s_school = models.CharField(max_length=100)
    s_email = models.EmailField()


# student_enrolment: db name