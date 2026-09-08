from django.shortcuts import render

from main.models import Experience


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
        "name": "Burhan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)