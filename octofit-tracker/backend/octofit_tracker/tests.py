from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create(email='test@example.com', name='Test User', team=team.name)
        self.assertEqual(user.email, 'test@example.com')

    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam2')
        self.assertEqual(team.name, 'TestTeam2')

    def test_activity_creation(self):
        team = Team.objects.create(name='TestTeam3')
        user = User.objects.create(email='test2@example.com', name='Test User2', team=team.name)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2024-01-01')
        self.assertEqual(activity.type, 'Run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='TestTeam4')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
