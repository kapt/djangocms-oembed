# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='OembedVideoPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('oembed_url', models.URLField(verbose_name='url')),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('autoplay', models.BooleanField(default=False)),
                ('show_related', models.BooleanField(default=False, help_text='hiding related videos is not supported by Vimeo (you need vimeo plus)')),
                ('loop', models.BooleanField(default=False, help_text='looping is not supported by YouTube')),
                ('type', models.CharField(default=b'', max_length=255, blank=True)),
                ('provider', models.CharField(default=b'', max_length=255, blank=True)),
                ('data', models.TextField(default=b'', blank=True)),
                ('html', models.TextField(default=b'', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
