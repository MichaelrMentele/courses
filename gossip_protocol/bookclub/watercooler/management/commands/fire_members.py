from django.core.management.base import BaseCommand, CommandError
import subprocess


class Command(BaseCommand):
    help = 'Fires everyone gossiping around the watercooler.'

    def handle(self, *args, **options):
        subprocess.run('pkill -f \'python manage.py runserver\'', shell=True)
        self.stdout.write(self.style.SUCCESS('All slackers fired!'))
