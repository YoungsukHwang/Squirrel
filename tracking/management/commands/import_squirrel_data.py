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
                reader2 = csv.DictReader(fp)
                data = list(reader2)

                print("Dict csv reader...")

                for item in data:
                    print(item)
                    s = Squirrel(
                            longitude=item['x'],
                            latitude=item['y'],
                            unique_squirrel_id=item['unique_squirrel_id'],
                            hectare=item['hectare'],
                            shift=item['shift'],
                            date=convert_date(item['date']),
                            hectare_squirrel_number=item['hectare_squirrel_number'],
                            age=item['age'],
                            primary_fur_color=item['primary_fur_color'],
                            location=item['location'],
                            specific_location=item['specific_location'],

                            running=('true'==item['running']),
                            chasing=('true'==item['chasing']),
                            climbing=('true'==item['climbing']),
                            eating=('true'==item['eating']),
                            foraging=('true'==item['foraging']),

                            other_activities=item['other_activities'],
                            
                            kuks=('true'==item['kuks']),
                            quaas=('true'==item['quaas']),
                            moans=('true'==item['moans']),
                            tail_flags=('true'==item['tail_flags']),
                            tail_twitches=('true'==item['tail_twitches']),
                            approaches=('true'==item['approaches']),
                            indifferent=('true'==item['indifferent']),
                            runs_from=('true'==item['runs_from']),
                    )
                    s.save()
                print("Done: Dict csv reader...")

            #with open(path) as f:
            #    reader = csv.reader(f)
            #    next(reader)

            #    print("Regular csv reader...")
            #    for row in reader:
            #        obj, created = Squirrel.objects.get_or_create(
            #                longitude = row[0],
            #                latitude = row[1],
            #                unique_squirrel_id = row[2],
            #                hectare = row[3],
            #                shift = row[4],
            #                date = "2019-12-12",
            #                hectare_squirrel_number = row[6],
            #                age = row[7],
            #                primary_fur_color = row[8],
            #                location = row[12],
            #                specific_location = row[14],
            #                running = False,#row[15],
            #                chasing = False,#row[16],
            #                climbing = False,#row[17],
            #                eating = False,#row[18],
            #                foraging = False,#row[19],
            #                other_activities = row[20],
            #                kuks = False,#row[21],
            #                quaas = False,#row[22],
            #                moans = False,#row[23],
            #                tail_flags = False,#row[24],
            #                tail_twitches = False,#row[25],
            #                approaches = False,#row[26],
            #                indifferent = False,#row[27],
            #                runs_from = False,#row[28],

            #                )
                print("Done:Regulart csv reader...")
        except:
            raise CommandError('Error with reading csv or creating objects')

        self.stdout.write(self.style.SUCCESS(f'Successfully imported csv file from {path}.' ))

def convert_date(eight_digits):
    "Change eight-digits input to YYYY-MM-DD format"
    month=eight_digits[0:2]
    day=eight_digits[2:4]
    year=eight_digits[4:]
    return f"{year}-{month}-{day}"


