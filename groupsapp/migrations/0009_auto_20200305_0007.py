# Generated by Django 3.0.2 on 2020-03-04 21:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('groupsapp', '0008_auto_20200220_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('c9b1c52a-9764-48b5-b2b7-5d3b7c3cfd05'), verbose_name='uuid'),
        ),
    ]