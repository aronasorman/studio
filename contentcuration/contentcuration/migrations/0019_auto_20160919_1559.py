# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 22:59
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0018_auto_20160919_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='mastery_model',
            field=models.CharField(choices=[(b'do-all', b'Do all'), (b'num_correct_in_a_row_10', b'10 in a row'), (b'num_correct_in_a_row_3',
                                                                                                                   b'3 in a row'), (b'num_correct_in_a_row_5', b'5 in a row'), (b'skill-check', b'Skill check')], default=b'do-all', max_length=200),
        ),
    ]
