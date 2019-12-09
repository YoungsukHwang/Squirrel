from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    def __str__(self):
        return (
            f"SQR!: {self.unique_squirrel_id} "
            f"{self.longitude} {self.latitude} {self.hectare} "
            f"{self.shift} {self.date} {self.hectare_squirrel_number} {self.age}\n"
        )

    longitude = models.DecimalField(
            help_text = _('Longitude Location'),
            max_digits=15,
            decimal_places=13,
            default='0',
    )

    latitude = models.DecimalField(
            help_text = _('Latitude Location'),
            max_digits=15,
            decimal_places=13,
            default='0',
    )

    unique_squirrel_id = models.CharField(
            help_text = _('Squirrel ID'),
            max_length=100,
            blank=True,
    )

    hectare = models.CharField(
            help_text = _('Hectare'),
            max_length=100,
            blank=True,
    )

    PM = 'pm'
    AM = 'am'
    OTHER=''

    SHIFT_CHOICES = (
        (PM, 'PM'),
        (AM, 'AM'),
        (OTHER, ''),
    )

    shift = models.CharField(
            help_text = _('Squirrels Shift'),
            max_length=2,
            choices=SHIFT_CHOICES,
            default=OTHER,
    )

    date = models.DateField(
        help_text=_('Date of sighting'),
        default='2000-01-01',
    )

    hectare_squirrel_number = models.IntegerField(\
            help_text = _('Number of the sighting session'),
            default='0',
    )
    
    ADULT = 'adult'
    JUVENILE = 'juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
            help_text = _('Age of squirrel'),
            max_length=10,
            choices=AGE_CHOICES,
            blank=True,
    )

    CINNAMON = 'cinnamon'
    WHITE = 'white'
    BLACK = 'balck'\

    PRIMARY_FUR_COLOR_CHOICES = (
        (CINNAMON, 'Cinnamon'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    )
    
    primary_fur_color = models.CharField(
            help_text = _('Primary fur color'),
            max_length=20,
            choices=PRIMARY_FUR_COLOR_CHOICES,
            blank=True,
    )

    ABOVE_GROUND = 'above ground'
    GROUND_PLANE = 'ground plane'


    LOCATION_CHOICES = (
        (ABOVE_GROUND, 'Above Ground'),
        (GROUND_PLANE, 'Ground Plane'),
    )

    location = models.CharField(
            help_text = _('Location of First Sight of the squirrel'),
            max_length=20,
            choices= LOCATION_CHOICES,
            blank=True,
    )
    
    specific_location = models.CharField(
            help_text = _('Specific Location'),
            max_length=100,
            blank=True,
    )

    running = models.BooleanField(
            help_text = _('Squirrel was seen running.'),
            default=False,
    )

    chasing = models.BooleanField(
            help_text = _('Squirrel was seen chasing another squirrel'),
            default=False,
    )

    climbing = models.BooleanField(
            help_text = _('Squirrel was seen climbing a tree or other environmental landmark'),
            default=False,
    )

    eating = models.BooleanField(
            help_text = _('Squirrel was seen eating'),
            default=False,
    )

    foraging = models.BooleanField(
            help_text = _('Squirrel was seen foraging for food'),
            default=False,
    )

    other_activities = models.CharField(
            help_text = _('Other Activities'),
            max_length=100,
            blank=True,
    )

    kuks = models.BooleanField(
            help_text = _('Squirrel was heard kukking'),
            default=False,
    )

    quaas = models.BooleanField(
            help_text = _('Squirrel was heard quaaing'),
            default=False,
    )

    moans = models.BooleanField(
            help_text = _('Squirrel was heard moaning'),
            default=False,
    )

    tail_flags = models.BooleanField(
            help_text = _('Squirrel was seen flagging its tail'),
            default=False,
    )

    tail_twitches = models.BooleanField(
            help_text = _('Squirrel was seen twitching its tail'),
            default=False,
    )

    approaches = models.BooleanField(
            help_text = _('Squirrel was seen approaching human'),
            default=False,
    )

    indifferent = models.BooleanField(
            help_text = _('Squirrel was indifferent to human presence'),
            default=False,
    )

    runs_from = models.BooleanField(
            help_text = _('Squirrel was seen running from humans'),
            default=False,
    )
