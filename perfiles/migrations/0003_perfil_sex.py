# Generated by Django 4.0.5 on 2022-07-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_perfil_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]