# Generated by Django 3.1.5 on 2021-01-22 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('guid', models.CharField(max_length=15)),
                ('platforms', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
