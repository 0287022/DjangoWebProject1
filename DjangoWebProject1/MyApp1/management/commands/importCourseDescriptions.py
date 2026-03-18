import csv
from django.core.management import BaseCommand
from MyApp1.models import courseDescription

class Command(BaseCommand):
    help = "Help me please"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, **kwargs):
        path=kwargs['path']
        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            for row in reader:
                count += 1
                print(row[0])
                courseDescription.objects.create(courseDesc=row[1])
            print('Added ' + str(count) + " courses")