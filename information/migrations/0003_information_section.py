# Generated by Django 4.0.5 on 2022-06-29 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information.section'),
        ),
    ]
