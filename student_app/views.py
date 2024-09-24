from django.shortcuts import render,redirect
from school.forms import Studform, SForm
from student_app.models import stud

# model - stud
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    title="New Student Registration"
    form=Studform(request.POST)
    if form.is_valid(): # Checks if the submitted data in form is valid
                        # Process the valid form data (e.g., save to the database)
        name=form.cleaned_data['s_name'] # get the  input values to variables
        cls=form.cleaned_data['s_class']
        addr=form.cleaned_data['s_addr']
        school=form.cleaned_data['s_school']
        mail=form.cleaned_data['s_email']

 # chk student already registered or not with email-id matching
        chk_email=stud.objects.filter(s_email=mail)

        if len(chk_email)>0: # to check student is in DB
            return render(request, 'ack.html', {"title": "Student already exists ... try with other email"})
        else:
            data=stud(s_name=name,s_class=cls,s_addr=addr,s_school=school,s_email=mail)
            data.save()
            return render(request,'ack.html',{"title":"Registered succesfuly"})
# or not-work need to check ---error
    # try:
        #     form.save()
        #     return render(request,'ack.html',{"title":"Registered succesfuly"})
        #     # return redirect('/register')
        # except:
        #     pass
    context={
        "title":title,
        "form":form,
            }
    return render(request,'register.html',context)

# to show the registured students
def existing(request):
    # print('hai fun exist')
    title="Registered Students List..."
    queryset=stud.objects.all()
    # print(queryset)
    context={"title":title,
             "queryset":queryset}
    print("hello")
    return render(request,'existing.html',context)

def search(request):
    # print("fun search")
    title="Search Student"
    form=SForm(request.POST or None)

    if form.is_valid():
        name=form.cleaned_data['s_name']

#filter data based on name
        queryset=stud.objects.filter(s_name=name)

#Check student is in the db or not
        if len(queryset)==0:
            return render(request, 'ack.html', {'title':"Student details not found... Please Enter correct name"})
        context = {"title": title,
                   "queryset": queryset}
        return render(request,'existing.html',context)
    context={
        "title":title,
        'form':form,
            }
    return render(request,'search.html', context)

# fun to delete the dropout student from DB

def dropout(request):
    title="Drop Out"
    form=SForm(request.POST or None)

    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name)

# search student is present or not
        if len(queryset)==0:    # if student not in DB then show a msg
            return render(request, 'ack.html', {'title':"Student details not found... Please Enter correct name"})

        else:   # if student in DB then  delete it
            queryset=stud.objects.filter(s_name=name).delete()
            return render(request, 'ack.html', {'title': "Student Removed From Database"})
    context={
        "title":title,
        'form':form,
            }
    return render(request,'search.html', context)