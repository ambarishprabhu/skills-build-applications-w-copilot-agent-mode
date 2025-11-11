from django.test import TestCase
from .models import User, Team

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Marvel", universe="Marvel")
        user = User.objects.create(email="tony@stark.com", name="Tony Stark", team=team)
        self.assertEqual(user.name, "Tony Stark")
