from django.core.management.base import BaseCommand

from source.models import Version


class Command(BaseCommand):
    args = '<identifier>'
    help = 'Imports the specified directory of files into the database.'

    def handle(self, identifier, *args, **options):
        version = Version.objects.get(identifier=identifier)
        version.delete()
