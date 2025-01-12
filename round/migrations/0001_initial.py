# Generated by Django 5.0.7 on 2024-07-14 21:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('round_number', models.CharField(max_length=35)),
                ('current', models.BooleanField(blank=True, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tournament', models.ForeignKey(limit_choices_to={'finished': False}, on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
