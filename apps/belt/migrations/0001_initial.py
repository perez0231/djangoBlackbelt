# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('plan', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_users', to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='itineraries',
            name='trips',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_planned', to='belt.Trip'),
        ),
        migrations.AddField(
            model_name='itineraries',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='going_user', to='login.User'),
        ),
    ]
