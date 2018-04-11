from django.core.management.base import BaseCommand, CommandError
import subprocess


class Command(BaseCommand):
    help = 'Adds someone new around the watercooler.'

    def add_arguments(self, parser):
        parser.add_argument('ports', nargs='+', type=int)

    def handle(self, *args, **options):
        for port in options['ports']:
            subprocess.run('python manage.py runserver %s &' % port, shell=True)
            self.stdout.write(
                self.style.SUCCESS(
                    'Someone new joined the converstion the slackers around'
                    'watercooler at port: "%s"' % port
                )
            )
