# Generated by Django 5.0.1 on 2024-12-22 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0004_featureditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureditem',
            name='user',
        ),
        migrations.AddField(
            model_name='featureditem',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='featured_items', to='myport.profile'),
            preserve_default=False,
        ),
    ]
