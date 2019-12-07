from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    longitude = models.DecimalField(
            help_text = _('Longitude Location'),
            max_digits=15,
            decimal_places=13,
    )

    latitude = models.DecimalField(
            help_text = _('Latitude Location'),
            max_digits=15,
            decimal_places=13,
    )

    unique_squirrel_id = models.CharField(
            help_text = _('Squirrel ID'),
            max_length=100,
    )

    hectare = models.CharField(
            help_text = _('Hectare'),
            max_length=100,
    )

    PM = 'pm'
    AM = 'am'
    OTHER=''

    SHIFT_CHOICES = (
        (PM, 'PM'),
        (AM, 'PM'),
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
    )

    hectare_squirrel_number = models.IntegerField(\
            help_text = _('Number of the sighting session'),
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
    )
    
    specific_location = models.CharField(
            help_text = _('Specific Location'),
            max_length=100,
    )

    running = models.BooleanField(
            help_text = _('Squirrel was seen running.'),
    )

    chasing = models.BooleanField(
            help_text = _('Squirrel was seen chasing another squirrel'),
    )

    climbing = models.BooleanField(
            help_text = _('Squirrel was seen climbing a tree or other environmental landmark'),
    )

    eating = models.BooleanField(
            help_text = _('Squirrel was seen eating'),
    )

    foraging = models.BooleanField(
            help_text = _('Squirrel was seen foraging for food'),
    )

    other_activities = models.CharField(
            help_text = _('Other Activities'),
            max_length=100,
    )

    kuks = models.BooleanField(
            help_text = _('Squirrel was heard kukking'),
    )

    quaas = models.BooleanField(
            help_text = _('Squirrel was heard quaaing'),
    )

    moans = models.BooleanField(
            help_text = _('Squirrel was heard moaning'),
    )

    tail_flags = models.BooleanField(
            help_text = _('Squirrel was seen flagging its tail'),
    )

    tail_twitches = models.BooleanField(
            help_text = _('Squirrel was seen twitching its tail'),
    )

    approaches = models.BooleanField(
            help_text = _('Squirrel was seen approaching human'),
    )

    indifferent = models.BooleanField(
            help_text = _('Squirrel was indifferent to human presence'),
    )

    runs_from = models.BooleanField(
            help_text = _('Squirrel was seen running from humans'),
    )
