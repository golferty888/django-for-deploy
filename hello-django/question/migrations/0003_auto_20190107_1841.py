# Generated by Django 2.2.dev20190102231945 on 2019-01-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_choice_question'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('question', 'title')},
        ),
    ]
