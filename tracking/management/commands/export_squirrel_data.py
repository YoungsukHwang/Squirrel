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
            squirrels=Squirrel.objects.all()

            with open(path, 'w') as csvfile:
                writer = csv.writer(csvfile)
                # write your header first
                header = 'ID,X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Location,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from'
                list_ = header.split(',')
                print(list_)

                writer.writerow(list_)

                for obj in squirrels:
                    writer.writerow(getattr(obj, field.name) for field in Squirrel._meta.fields)
        except:
            raise CommandError('Error with exporting csv.')
            
        self.stdout.write(self.style.SUCCESS(f'Successfully exported csv file from {path}.' ))
