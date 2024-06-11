# Generated by Django 5.0.4 on 2024-04-30 10:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='name',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='name'),
            preserve_default=False,
        ),
    ]
