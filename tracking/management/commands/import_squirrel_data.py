from django.core.management.base import BaseCommand, CommandError

from tracking.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'To import the csv file to the django database'

    def add_arguments(self, parser):
        parser.add_argument('/path/to/file.csv', type=str)

    def handle(self, *args, **options):

        path = options['/path/to/file.csv']
        print("Reading path...:" + path)

        try:
            with open(path) as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    obj, created = Squirrel.objects.get_or_create(
                            longitude = row[0],
                            latitude = row[1],
                            unique_squirrel_id = row[2],
                            hectare = row[3],
                            shift = row[4],
                            date = "2019-12-12",
                            hectare_squirrel_number = row[6],
                            age = row[7],
                            primary_fur_color = row[8],
                            location = row[12],
                            specific_location = row[14],
                            running = False,#row[15],
                            chasing = False,#row[16],
                            climbing = False,#row[17],
                            eating = False,#row[18],
                            foraging = False,#row[19],
                            other_activities = row[20],
                            kuks = False,#row[21],
                            quaas = False,#row[22],
                            moans = False,#row[23],
                            tail_flags = False,#row[24],
                            tail_twitches = False,#row[25],
                            approaches = False,#row[26],
                            indifferent = False,#row[27],
                            runs_from = False,#row[28],

                            )
        except:
            raise CommandError('Error with reading csv or creating objects')

        self.stdout.write(self.style.SUCCESS(f'Successfully imported csv file from {path}.' ))



#import csv
#
#class Importing(BaseCommand):
#    def 
#    with open(path) as f:
#        reader = csv.reader(f)
#        for row in reader:
#            _, created = Teacher.objects.get_or_create(
#                first_name=row[0],
#                last_name=row[1],
#                middle_name=row[2],
#             )
