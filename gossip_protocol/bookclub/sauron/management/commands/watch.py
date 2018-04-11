from django.core.management.base import BaseCommand, CommandError
import subprocess


class Command(BaseCommand):
    help = 'Spin up sauron to watch.'

    def handle(self, *args, **options):
        subprocess.run('python manage.py runserver', shell=True)
        self.stdout.write(
            self.style.SUCCESS('Sauron is watching!')
        )
