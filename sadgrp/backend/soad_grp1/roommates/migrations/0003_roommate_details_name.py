# Generated by Django 3.0.8 on 2020-10-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0002_roommate_details_food_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommate_details',
            name='name',
            field=models.CharField(default='user', max_length=264),
            preserve_default=False,
        ),
    ]
