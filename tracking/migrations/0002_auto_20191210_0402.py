# Generated by Django 2.2.7 on 2019-12-10 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(blank=True, choices=[('pm', 'PM'), ('am', 'AM'), ('', '')], default='', help_text='Squirrels Shift', max_length=2),
        ),
    ]
