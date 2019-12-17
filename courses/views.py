from django.shortcuts import render, get_object_or_404
from .models import Course, Student
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/courses/')
        else:
            return render(request, 'courses/login.html', {'error': "Invalid Credentials"})
    return render(request, 'courses/login.html')


def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            first_name=request.POST['first_name'] ,
            email=request.POST['email'],
            password=request.POST['password'],
            username=request.POST['username']
        )
        return HttpResponseRedirect('/courses/login/')
    return render(request, 'courses/register.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/course/login/')


@login_required(login_url='/courses/login/')
def home(request):
    student_list = Student.objects.all()
    return render(request, 'courses/home.html', {'student_list': student_list})


@login_required(login_url='/courses/login/')
def create_student(request):
    course_list = Course.objects.all()
    if request.method == 'POST':
        course = Course.objects.get(course_name=request.POST['course'])
        Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            dob=request.POST['dob'],
            tools=request.POST['tools'],
            image=request.FILES['image'],
            course=course
        )
        return HttpResponseRedirect('/courses/')
    return render(request, 'courses/create.html', {'course_list': course_list})


@login_required(login_url='/courses/login/')
def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'courses/details.html', {'student': student})


@login_required(login_url='/courses/login/')
def edit_view(request, student_id):
    course_list = Course.objects.all()
    stu = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        stu.course = Course.objects.get(course_name=request.POST['course'])
        stu.first_name = request.POST['first_name']
        stu.last_name = request.POST['last_name']
        stu.email = request.POST['email']
        stu.phone = request.POST['phone']
        stu.tools = request.POST['tools']
        stu.save()
        return HttpResponseRedirect('/courses/')
    return render(request, 'courses/edit.html', {'stu': stu,
                                                 'course_list': course_list})


def delete_view(request, stu_id):
    s = Student.objects.get(pk=stu_id)
    s.delete()
    return HttpResponseRedirect('/courses/')
