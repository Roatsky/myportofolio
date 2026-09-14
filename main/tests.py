from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education, Skills


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            thumbnail="\\static\\img\\PBP.png"
        )
        self.education = Education.objects.create(
            title="Fasilkom UI",
            category="tertiary",
            thumbnail="\\static\\img\\CSUI.png"
        )
        self.skill = Skills.objects.create(
            title="Koding",
            description="Berpengalam dalam koding di java dan python.",
            category="hard-skills",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.description, "Membantu mahasiswa memahami pengembangan web.")
        self.assertEqual(self.experience.category, "part-time")
        self.assertEqual(self.experience.thumbnail, "\\static\\img\\PBP.png")
        self.assertTrue(self.experience.is_ongoing)

    def test_education_model(self):
        self.assertEqual(str(self.education), "Fasilkom UI")
        self.assertEqual(self.education.category, "tertiary")
        self.assertEqual(self.education.thumbnail, "\\static\\img\\CSUI.png")
        self.assertTrue(self.education.is_ongoing)

    def test_skills_model(self):
        self.assertEqual(str(self.skill), "Koding")
        self.assertEqual(self.skill.description, "Berpengalam dalam koding di java dan python.")
        self.assertEqual(self.skill.category, "hard-skills")

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.title)
        self.assertContains(response, "Tertiary")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_skills_page(self):
        response = self.client.get(reverse("main:show_skills"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")
        self.assertContains(response, self.skill.title)
        self.assertContains(response, self.skill.description)
        self.assertContains(response, "Hard-Skills")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Belum ada pendidikan yang ditambahkan.")

    def test_empty_skills_page(self):
        Skills.objects.all().delete()
        response = self.client.get(reverse("main:show_skills"))

        self.assertContains(response, "Belum ada keterampilan yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_completed_education(self):
        self.education.ended_at = timezone.now()
        self.education.save()
        response = self.client.get(reverse("main:show_education"))

        self.assertFalse(self.education.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")