# Generated by Django 5.0.7 on 2024-07-14 21:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_myapply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=100)),
                ('PubgName', models.CharField(max_length=100)),
                ('PubgID', models.CharField(max_length=20)),
                ('point', models.IntegerField(blank=True, default=0, null=True)),
                ('played', models.IntegerField(blank=True, default=0, null=True)),
                ('win', models.IntegerField(blank=True, default=0, null=True)),
                ('lose', models.IntegerField(blank=True, default=0, null=True)),
                ('trophy', models.IntegerField(blank=True, default=0, null=True)),
                ('joined', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
