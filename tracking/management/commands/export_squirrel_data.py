import csv

from django.core.management.base import BaseCommand, CommandError

from tracking.models import Squirrel


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
                h1 = 'ID,X,Y,Unique Squirrel ID,Hectare,Shift,Date,'
                h2 = 'Hectare Squirrel Number,Age,Primary Fur Color,Location,'
                h3 = 'Specific Location,Running,Chasing,Climbing,Eating,'
                h4 = 'Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,'
                h5 = 'Tail twitches,Approaches,Indifferent,Runs from'
                header = h1+h2+h3+h4+h5

                list_ = header.split(',')
                writer.writerow(list_)

                for obj in squirrels:
                    writer.writerow(getattr(obj, field.name) for field in Squirrel._meta.fields)
        except:
            raise CommandError('Error with exporting csv.')
            
        self.stdout.write(self.style.SUCCESS(f'Success export from {path}.'))

