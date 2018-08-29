# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import light_gallery.validators


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0016_auto_20180802_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='thumbnail_background_color',
            field=models.CharField(blank=True, max_length=7, validators=[light_gallery.validators.validate_hex], verbose_name='Thumbnail box background color (in form #a0b1c2)'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbnail_border_color',
            field=models.CharField(blank=True, max_length=7, validators=[light_gallery.validators.validate_hex], verbose_name='Border color (in form #a0b1c2)'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbnail_border_size',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Width of thumbnail border (in pixels)'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbnail_orientation',
            field=models.CharField(choices=[[b'v', b'Vertical'], [b'h', b'Horizontal (text on right)'], [b'hr', b'Horizontal (text on left)'], [b'c', b'Columns']], default=b'v', max_length=2, verbose_name='Orientation of thumbnail elements'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbnail_padding_size',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Thickness of thumbnail padding (in pixels)'),
        ),
    ]
