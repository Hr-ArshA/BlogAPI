from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of my custom command'

    def handle(self, *args, **options):
        # Code for your custom command goes here
        self.stdout.write('My custom command executed successfully')