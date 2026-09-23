from django.urls import path

from main.views import show_main, show_experience, show_education, show_skills, create_project, show_project, get_projects_json, delete_project, get_experience_json, delete_experience, create_experience, get_education_json, delete_education, create_education, get_skills_json, delete_skills, create_skills, register, login_user, logout_user, project_star, education_star, skills_star, experience_star

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
    path("education/add/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("skills/add/", create_skills, name="create_skills"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:skills_id>/delete/",delete_skills,name="delete_skills"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", project_star,name="project_star",),
    path("experience/<uuid:experience_id>/star/", experience_star,name="experience_star",),
    path("education/<uuid:education_id>/star/", education_star,name="education_star",),
    path("skills/<uuid:skills_id>/star/", skills_star,name="skills_star",),
]