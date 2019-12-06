from django.core.management.base import BaseCommand, CommandError

from tracking.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'To export the csv file from the django database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):

        path = options['file_path']
        print("Exporting on the path...:" + path)

        try:
            with open(path, 'w') as csvfile:
                writer = csv.writer(csvfile)
                # write your header first
                for obj in Squirrel.objects.all():
                    writer.writerow(getattr(obj, field.name) for field in Squirrel._meta.fields)
        except:
            raise CommandError('Error with exporting csv.')
            
        self.stdout.write(self.style.SUCCESS(f'Successfully exported csv file from {path}.' ))


                #for row in reader:
                #    obj, created = Squirrel.objects.get_or_create(
                #            longitude = row[0],
                #            latitude = row[1],
                #            unique_squirrel_id = row[2],
                #            hectare = row[3],
                #            shift = row[4],
                #            date = "2019-12-12",
                #            hectare_squirrel_number = row[6],
                #            age = row[7],
                #            primary_fur_color = row[8],
                #            location = row[12],
                #            specific_location = row[14],
                #            )

