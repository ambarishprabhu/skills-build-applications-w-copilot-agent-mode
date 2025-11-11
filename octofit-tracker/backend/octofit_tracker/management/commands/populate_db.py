from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Create users (super heroes)
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30)
        Activity.objects.create(user=steve, type='Cycling', duration=45)
        Activity.objects.create(user=bruce, type='Swimming', duration=60)
        Activity.objects.create(user=clark, type='Yoga', duration=20)

        # Create workouts
        Workout.objects.create(user=tony, description='Chest day', date='2025-11-10')
        Workout.objects.create(user=steve, description='Leg day', date='2025-11-09')
        Workout.objects.create(user=bruce, description='Cardio', date='2025-11-08')
        Workout.objects.create(user=clark, description='Strength', date='2025-11-07')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
