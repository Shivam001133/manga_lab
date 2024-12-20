# Generated by Django 5.0.9 on 2024-11-23 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mangavault', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/BannerImages/')),
                ('image_url', models.URLField(blank=True)),
                ('source_type', models.CharField(choices=[('image', 'Image'), ('video', 'video')], default='image', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banner_image', to='mangavault.mangavault')),
            ],
        ),
    ]
