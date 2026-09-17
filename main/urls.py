from django.urls import path

from main.views import show_main, show_experience, show_education, show_skills, create_project, show_project, get_projects_json, delete_project, get_experience_json, delete_experience, create_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("education/", show_education, name="show_education"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_project, name="show_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
]