from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Eliminar datos previos
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='superhero', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='superhero', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='superhero', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='superhero', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)
        Activity.objects.create(user=superman, type='Swimming', duration=60)
        Activity.objects.create(user=captain, type='Walking', duration=20)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=80)
        Leaderboard.objects.create(user=captain, points=70)

        # Crear workouts
        Workout.objects.create(user=ironman, description='Pushups', reps=50)
        Workout.objects.create(user=batman, description='Situps', reps=40)
        Workout.objects.create(user=superman, description='Squats', reps=60)
        Workout.objects.create(user=captain, description='Pullups', reps=30)

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con datos de prueba.'))
