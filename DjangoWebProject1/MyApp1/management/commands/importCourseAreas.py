import csv
from django.core.management import BaseCommand
from MyApp1.models import courseArea

class Command(BaseCommand):
    help = "Help me please"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path=kwargs['path']
        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            for row in reader:
                count += 1
                courseArea.objects.create(courseArea=row[0], course=row[1])
            print('Added ' + str(count) + " courses")