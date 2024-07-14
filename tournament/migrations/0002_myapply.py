# Generated by Django 5.0.7 on 2024-07-14 21:10

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyApply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=80)),
                ('PubgName', models.CharField(max_length=50)),
                ('PubgID', models.CharField(max_length=20)),
                ('tgusername', models.CharField(blank=True, max_length=50, null=True)),
                ('applydate', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('tournament_name', models.ForeignKey(limit_choices_to={'finished': False}, on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
    ]