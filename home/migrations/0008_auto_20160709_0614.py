# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 06:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160709_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())], blank=True, default=''),
        ),
    ]
