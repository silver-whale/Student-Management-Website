from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from .forms import StudentsForm
from django.urls import reverse
from django.db import connection
from django.contrib import messages


def home(request):
    students = Students.objects.all()
    return render(request, 'myApp/home.html', {"students" : students})

def addStudent(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = StudentsForm()
    return render(request, "myApp/input.html", {'form':form})

def delete(request, student_id_num):
    student = get_object_or_404(Students,pk=student_id_num)
    student.delete()
    return redirect('home')

def edit(request, student_id_num):
    
    student = get_object_or_404(Students,pk=student_id_num)

    if request.method == "POST":
            student.firstname = request.POST['firstname']
            student.secondname = request.POST['secondname']
            student.age = request.POST['age']
            student.major = request.POST['major']
            student.address = request.POST['address']
            student.save()
            return redirect('home')
    else:
        form = StudentsForm(instance=student)
        context={
            'form':form,
            'writing':True,
            'now':'edit',
        }
        return render(request, "myApp/edit.html", {'form':form})

def search(request):
    students = Students.objects.all()
    output = []
    if request.method == "POST":
        searchID = request.POST.get('searchID')
        if searchID == None:
            return render(request, 'myApp/home.html', {"students" : students})

    with connection.cursor() as cursor:
        query = "SELECT ID_num, Firstname, Secondname, Age, Major, Address  \
                FROM students \
                WHERE ID_num = %s"
        cursor.execute(query, searchID)
        fetchResult = cursor.fetchall()
    connection.commit()
    connection.close()

    for temp in fetchResult:
        eachRow = {'id_num':temp[0], 'firstname':temp[1], 'secondname':temp[2], 'age':temp[3], \
                    'major':temp[4], 'address':temp[5]}
        output.append(eachRow)

    return render(request, "myApp/search.html", {"output":output})

