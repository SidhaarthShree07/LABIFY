# Generated by Django 5.0.1 on 2024-03-05 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_posting'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='post',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='myapp.post'),
            preserve_default=False,
        ),
    ]
