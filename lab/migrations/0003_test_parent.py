# Generated by Django 5.1.3 on 2025-02-20 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_remove_appointmenttest_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lab.test'),
        ),
    ]
