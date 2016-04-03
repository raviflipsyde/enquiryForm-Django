# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryforms', '0002_auto_20150430_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicenquiryform',
            name='birth_date',
            field=models.DateTimeField(verbose_name='Birth Date', null=True),
        ),
        migrations.AddField(
            model_name='basicenquiryform',
            name='ssc_rollno',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
