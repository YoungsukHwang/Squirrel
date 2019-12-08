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

                            running=('true'==item['Running']),
                            chasing=('true'==item['Chasing']),
                            climbing=('true'==item['Climbing']),
                            eating=('true'==item['Eating']),
                            foraging=('true'==item['Foraging']),

                            other_activities=item['Other Activities'],
                            
                            kuks=('true'==item['Kuks']),
                            quaas=('true'==item['Quaas']),
                            moans=('true'==item['Moans']),
                            tail_flags=('true'==item['Tail flags']),
                            tail_twitches=('true'==item['Tail twitches']),
                            approaches=('true'==item['Approaches']),
                            indifferent=('true'==item['Indifferent']),
                            runs_from=('true'==item['Runs from']),
                    )
                    s.save()
                print("Done: Dict csv reader...")
                print(f"Total {i} rows has been updated.")
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
                print("done")
        except:
            raise CommandError('Error with reading csv or creating objects')

        self.stdout.write(self.style.SUCCESS(f'Successfully imported csv file from {path}.' ))

def convert_date(eight_digits):
    "Change eight-digits input to YYYY-MM-DD format"
    month=eight_digits[0:2]
    day=eight_digits[2:4]
    year=eight_digits[4:]
    return f"{year}-{month}-{day}"


