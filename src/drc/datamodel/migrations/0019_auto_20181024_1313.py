# Generated by Django 2.0.6 on 2018-10-24 13:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0018_auto_20181010_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectinformatieobject',
            name='registratiedatum',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 10, 24, 13, 13, 10, 318353, tzinfo=utc), help_text='De datum waarop de behandelende organisatie het INFORMATIEOBJECT heeft geregistreerd bij het OBJECT. Geldige waardes zijn datumtijden gelegen op of voor de huidige datum en tijd.', verbose_name='registratiedatum'),
            preserve_default=False,
        ),
    ]
