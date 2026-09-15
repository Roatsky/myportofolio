from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Skills, Project
from main.forms import ProjectForm

def show_main(request):
    context = {
        "name": "Muhammad Naufal Syarifuddin",
        "npm": "2506602896",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "CS student at Universitas Indonesia on his 3rd semester," 
            "yet the will and determination for IS course still as strong as in the 1st semester."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Naufal Syarifuddin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Muhammad Naufal Syarifuddin",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_skills(request):
    context = {
        "name": "Muhammad Naufal Syarifuddin",
        "skills_list": Skills.objects.all(),
    }
    return render(request, "skills.html", context)

def show_project(request):
    context = {
        "name": "Burhan",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)