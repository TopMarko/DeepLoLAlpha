# Generated by Django 3.0.5 on 2020-04-12 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200412_1826'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='summoner',
            unique_together={('region', 'accountId'), ('region', 'name'), ('region', 'summonerId')},
        ),
    ]