from django import forms
from student_app.models import stud
# class Studform(forms.ModelForm):
    #
    # class Meta:
    #      model= stud
    #     fields= "__all__"
# #     # fields=["s_name"]

#  OR
class Studform(forms.Form):
    s_name=forms.CharField(max_length=30,label='Student Name')
    s_class=forms.CharField(max_length=30,label='Class')
    s_addr = forms.CharField(max_length=30,label="Address")
    s_school = forms.CharField(max_length=30,label='School Name')
    s_email = forms.EmailField(label='E-mail')

class SForm(forms.Form): # for search
    s_name = forms.CharField(max_length=30, label=" Enter Student Name")


