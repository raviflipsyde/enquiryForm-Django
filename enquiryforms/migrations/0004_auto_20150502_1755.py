# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryforms', '0003_auto_20150502_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicenquiryform',
            name='birth_date',
            field=models.DateField(verbose_name='Birth Date', null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='enq_date',
            field=models.DateField(verbose_name='Enquiry Date'),
        ),
    ]
