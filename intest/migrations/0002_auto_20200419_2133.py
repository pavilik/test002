# Generated by Django 3.0.5 on 2020-04-19 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='surdname',
            new_name='surname',
        ),
    ]
