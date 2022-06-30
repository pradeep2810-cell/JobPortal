# Generated by Django 4.0.5 on 2022-06-28 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('estd', models.DateField()),
                ('address', models.TextField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('logo', models.ImageField(upload_to='organizations')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.category')),
            ],
        ),
    ]
