import csv

from django.core.management.base import BaseCommand, CommandError

from tracking.models import Squirrel


class Command(BaseCommand):
    help = 'To import the csv file to the django database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):

        path = options['csv_file_path']
        print("Reading path...:" + path)

        try:
            with open(path) as fp:
                print('Hi')
                reader2 = csv.DictReader(fp)
                data = list(reader2)

                print(f"Dict csv reader... The size: {len(data)}")
                i=0
                for item in data:
                    i+=1
                    s = Squirrel(
                            longitude=item['X'],
                            latitude=item['Y'],
                            unique_squirrel_id=item['Unique Squirrel ID'],
                            hectare=item['Hectare'],
                            shift=item['Shift'],
                            date=convert_date(item['Date']),
                            hectare_squirrel_number=item['Hectare Squirrel Number'],
                            age=item['Age'],
                            primary_fur_color=item['Primary Fur Color'],
                            location=item['Location'],
                            specific_location=item['Specific Location'],

                            running=('true'==item['Running'].lower()),
                            chasing=('true'==item['Chasing'].lower()),
                            climbing=('true'==item['Climbing'].lower()),
                            eating=('true'==item['Eating'].lower()),
                            foraging=('true'==item['Foraging'].lower()),

                            other_activities=item['Other Activities'],
                            
                            kuks=('true'==item['Kuks'].lower()),
                            quaas=('true'==item['Quaas'].lower()),
                            moans=('true'==item['Moans'].lower()),
                            tail_flags=('true'==item['Tail flags'].lower()),
                            tail_twitches=('true'==item['Tail twitches'].lower()),
                            approaches=('true'==item['Approaches'].lower()),
                            indifferent=('true'==item['Indifferent'].lower()),
                            runs_from=('true'==item['Runs from'].lower()),
                    )
                    s.save()
                print("Done: Dict csv reader...")
                print(f"Total {i} rows has been updated.")
                print("done")
        except:
            raise CommandError('Error with reading csv or creating objects')

        self.stdout.write(self.style.SUCCESS(f'Success import from {path}.'))


def convert_date(string):
    "Change eight-digits input to YYYY-MM-DD format"
    """YYYY-MM-DD -> YYYY-MM-DD"""
    if len(string)==8:
        eight_digits=string
        month=eight_digits[0:2]
        day=eight_digits[2:4]
        year=eight_digits[4:]
        return f"{year}-{month}-{day}"
    else:
        return string

