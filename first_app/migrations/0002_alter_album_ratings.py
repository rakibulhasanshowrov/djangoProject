# Generated by Django 4.2 on 2024-05-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='ratings',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
