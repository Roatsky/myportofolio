import json
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Experience, Education, Skills, Project


class PortfolioTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin_naufal",
            email="admin@example.com",
            password="password123",
        )
        self.regular_user = User.objects.create_user(
            username="visitor",
            email="visitor@example.com",
            password="password123",
        )

        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            thumbnail="https://example.com/pbp.png",
        )
        self.education = Education.objects.create(
            title="Fasilkom UI",
            category="tertiary",
            thumbnail="https://example.com/csui.png",
        )
        self.skill = Skills.objects.create(
            title="Koding",
            description="Berpengalaman dalam koding di Java dan Python.",
            category="hard-skills",
        )
        self.project = Project.objects.create(
            title="Tanampedia",
            description="Platform komunitas urban farming berbasis web.",
            tech_stack="Django, Python, JavaScript",
            project_url="https://github.com/Roatsky/tanampedia",
            project_image_url="https://example.com/tanampedia.png",
        )

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

        self.experience.ended_at = timezone.now()
        self.experience.save()
        self.assertFalse(self.experience.is_ongoing)

    def test_education_model(self):
        self.assertEqual(str(self.education), "Fasilkom UI")
        self.assertEqual(self.education.category, "tertiary")
        self.assertTrue(self.education.is_ongoing)

        self.education.ended_at = timezone.now()
        self.education.save()
        self.assertFalse(self.education.is_ongoing)

    def test_skills_model(self):
        self.assertEqual(str(self.skill), "Koding")
        self.assertEqual(self.skill.category, "hard-skills")

    def test_project_model(self):
        self.assertEqual(str(self.project), "Tanampedia")
        self.assertEqual(self.project.tech_stack, "Django, Python, JavaScript")

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Muhammad Naufal Syarifuddin")
        self.assertContains(response, "2506602896")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_page_renders_shell(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")

    def test_education_page_renders_shell(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, "Belum ada pendidikan yang ditambahkan atau ditemukan.")

    def test_skills_page_renders_shell(self):
        response = self.client.get(reverse("main:show_skills"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")
        self.assertContains(response, "Belum ada keterampilan yang ditambahkan atau ditemukan.")

    def test_get_projects_json(self):
        response = self.client.get(reverse("main:get_projects_json"))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], "Tanampedia")

    def test_get_experience_json(self):
        response = self.client.get(reverse("main:get_experience_json"))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], "Asisten Dosen PBP")

    def test_get_education_json(self):
        response = self.client.get(reverse("main:get_education_json"))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], "Fasilkom UI")

    def test_get_skills_json(self):
        response = self.client.get(reverse("main:get_skills_json"))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], "Koding")

    def test_get_projects_json_search_filter(self):
        response = self.client.get(reverse("main:get_projects_json"), {"title": "Tanam"})
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)

        response_empty = self.client.get(reverse("main:get_projects_json"), {"title": "TidakAda"})
        data_empty = json.loads(response_empty.content)
        self.assertEqual(len(data_empty), 0)

    def test_create_project_ajax_forbidden_for_non_superuser(self):
        self.client.login(username="visitor", password="password123")
        response = self.client.post(
            reverse("main:create_project_ajax"),
            {
                "title": "Project Baru",
                "description": "Deskripsi",
                "tech_stack": "Python",
            },
        )
        self.assertEqual(response.status_code, 403)

    def test_create_project_ajax_success_for_superuser(self):
        self.client.login(username="admin_naufal", password="password123")
        response = self.client.post(
            reverse("main:create_project_ajax"),
            {
                "title": "Portfolio V2",
                "description": "Website portofolio interaktif",
                "tech_stack": "Django, Fetch API",
                "project_url": "https://github.com/Roatsky",
                "project_image_url": "https://example.com/img.png",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Project.objects.filter(title="Portfolio V2").exists())

    def test_create_experience_ajax_success_for_superuser(self):
        self.client.login(username="admin_naufal", password="password123")
        response = self.client.post(
            reverse("main:create_experience_ajax"),
            {
                "title": "Software Engineer Intern",
                "description": "Mengembangkan layanan backend.",
                "category": "internship",
                "thumbnail": "https://example.com/intern.png",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Experience.objects.filter(title="Software Engineer Intern").exists())

    def test_create_education_ajax_success_for_superuser(self):
        self.client.login(username="admin_naufal", password="password123")
        response = self.client.post(
            reverse("main:create_education_ajax"),
            {
                "title": "SMA Negeri",
                "category": "secondary",
                "thumbnail": "https://example.com/sma.png",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Education.objects.filter(title="SMA Negeri").exists())

    def test_create_skills_ajax_success_for_superuser(self):
        self.client.login(username="admin_naufal", password="password123")
        response = self.client.post(
            reverse("main:create_skills_ajax"),
            {
                "title": "Public Speaking",
                "description": "Komunikasi efektif dalam tim.",
                "category": "soft-skills",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Skills.objects.filter(title="Public Speaking").exists())

    def test_ajax_strip_tags_rejects_html_only_title(self):
        self.client.login(username="admin_naufal", password="password123")
        response = self.client.post(
            reverse("main:create_project_ajax"),
            {
                "title": "<script></script><b>   </b>",
                "description": "Deskripsi valid",
                "tech_stack": "Django",
            },
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("title", data["errors"])

    def test_star_and_unstar_project(self):
        self.client.login(username="visitor", password="password123")
        star_url = reverse("main:project_star", args=[self.project.id])

        # Star
        self.client.post(star_url)
        self.assertIn(self.regular_user, self.project.starred_by.all())

        # Unstar
        self.client.post(star_url)
        self.assertNotIn(self.regular_user, self.project.starred_by.all())

    def test_delete_experience_by_superuser(self):
        self.client.login(username="admin_naufal", password="password123")
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())

    def test_delete_forbidden_for_regular_user(self):
        self.client.login(username="visitor", password="password123")
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Experience.objects.filter(id=self.experience.id).exists())