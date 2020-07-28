"""Custom Command"""
# django
from django.core.management.base import BaseCommand, CommandError

# Script
from export_data import ExportData


class Command(BaseCommand):
    help = 'Load csv data'

    def handle(self, *args, **options):
        #try:
        ExportData()
        #except:
        #raise CommandError('something goes wrong')
        self.stdout.write(self.style.SUCCESS('the data was load'))
