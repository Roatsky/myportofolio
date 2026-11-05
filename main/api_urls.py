from django.urls import path
from . import api_views

app_name = "api"
urlpatterns = [
    path("skills/", api_views.skills_list, name="skills-list"),
    path("skills/<uuid:skills_id>/", api_views.skills_detail, name="skills-detail"),
    path("skills/<uuid:skills_id>/star/", api_views.skills_star, name="skills-star"),
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),
    path("education/", api_views.education_list, name="education-list"),
    path("education/<uuid:education_id>/", api_views.education_detail, name="education-detail"),
    path("education/<uuid:education_id>/star/", api_views.education_star, name="education-star"),
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
]