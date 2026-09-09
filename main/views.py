from django.shortcuts import render

from main.models import Experience, Education, Skills


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