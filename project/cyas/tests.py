from django.test import TestCase
from .models import Project, Survey
from django.core.exceptions import ValidationError

class ProjectTestCase(TestCase):
    def test_project_create(self):
        p = Project(title="SpicyTaco")
        self.assertEqual(str(p), "SpicyTaco")


class SurveyTestCase(TestCase):
    def test_unique_choices(self):
        p = Project(title="SpicyTaco")
        p.save()

        s = Survey(name="TestUser", project1=p, project2=p)
        self.assertRaises(ValidationError, s.clean)

    def test_works(self):
        p1 = Project(title="SpicyTaco")
        p2 = Project(title="Other")
        p1.save()
        p2.save()

        s = Survey(name="TestUser", project1=p1, project2=p2)
        s.clean()
        s.save()
