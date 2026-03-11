import csv
from django.core.management import BaseCommand
from MyApp1.models import teacher

class Command(BaseCommand):
    help = "Help me please"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path=kwargs['path']
        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')
            teacher_count = 0
            for row in reader:
                teacher_count += 1
                teacher.objects.create(Name=row[0], Area=row[1])
            print('Added ' + str(teacher_count) + " teachers")