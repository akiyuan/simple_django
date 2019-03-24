# Generated by Django 2.1 on 2018-08-16 16:03

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('news', '0012_auto_20180815_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=taggit.managers.TaggableManager(
                help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
