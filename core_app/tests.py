from django.test import TestCase
from .models import Company_Story


class TestCase(TestCase):

    def test_story_creates(self):
        title = " alhasif company "
        prograph = "we work as a team base company for software soulations"
        prograph2 = "  our services are complete  identity of te companies and small businesses oners"
        story = Company_Story.objects.create(title=title, p1=prograph, p2=prograph2)
        self.assertEqual(str(story.title), title)

