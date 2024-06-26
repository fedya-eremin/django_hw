# Generated by Django 5.0.4 on 2024-04-23 21:27

import uuid

import django.db.models.deletion
from django.db import migrations, models

import repository.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=repository.models.get_datetime, null=True, validators=[repository.models.check_date_created], verbose_name='created')),
                ('name', models.TextField(verbose_name='name')),
            ],
            options={
                'verbose_name': 'developer',
                'verbose_name_plural': 'developers',
                'db_table': '"django_hw"."developer"',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('stars', models.PositiveIntegerField(default=0, verbose_name='stars')),
                ('developers', models.ManyToManyField(related_name='repository_developer', to='repository.developer')),
            ],
            options={
                'verbose_name': 'repository',
                'verbose_name_plural': 'repositories',
                'db_table': '"django_hw"."repository"',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='description')),
                ('status', models.TextField(choices=[('created', 'created'), ('in work', 'in work'), ('done', 'done')], verbose_name='status')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
                'db_table': '"django_hw"."ticket"',
            },
        ),
    ]
