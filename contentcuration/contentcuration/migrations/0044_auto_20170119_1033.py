# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-19 18:33
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0043_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatpreset',
            name='id',
            field=models.CharField(choices=[('high_res_video', 'High Resolution'), ('low_res_video', 'Low Resolution'), ('vector_video', 'Vectorized'), ('video_thumbnail', 'Thumbnail'), ('video_subtitle', 'Subtitle'), ('audio', 'Audio'), ('audio_thumbnail', 'Thumbnail'), ('document', 'Document'), ('document_thumbnail', 'Thumbnail'), (
                'exercise', 'Exercise'), ('exercise_thumbnail', 'Thumbnail'), ('exercise_image', 'Exercise Image'), ('exercise_graphie', 'Exercise Graphie'), ('channel_thumbnail', 'Channel Thumbnail'), ('html5_zip', 'HTML5 Zip'), ('html5_thumbnail', 'HTML5 Thumbnail')], max_length=150, primary_key=True, serialize=False),
        ),
    ]
