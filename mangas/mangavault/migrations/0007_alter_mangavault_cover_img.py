# Generated by Django 5.0.9 on 2024-11-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangavault', '0006_alter_mangavault_cover_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangavault',
            name='cover_img',
            field=models.URLField(blank=True, null=True),
        ),
    ]
