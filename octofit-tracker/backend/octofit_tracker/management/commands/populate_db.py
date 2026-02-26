from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team=marvel.name, is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team=marvel.name, is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name, is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team=dc.name, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name='Super Strength', description='Heavy lifting workout', difficulty='Hard'),
            Workout(name='Flight Training', description='Aerobic and agility', difficulty='Medium'),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='Strength', duration=60, date=timezone.now())
        Activity.objects.create(user=users[1], type='Cardio', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], type='Stealth', duration=30, date=timezone.now())
        Activity.objects.create(user=users[3], type='Flight', duration=50, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
