# Generated by Django 5.0.9 on 2024-11-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangavault', '0002_mangavault_manga_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangavault',
            name='manga_title',
            field=models.TextField(default=list),
        ),
    ]
