# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicenquiryform',
            name='address_home',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='career_choice',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='contact_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='contact_no_home',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='contact_no_primary',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='father_contact_home',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='father_contact_primary',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='father_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='ssc_aggregate',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='ssc_classes',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='ssc_maths',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='ssc_percent',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='ssc_school',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='ssc_science',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='student_fname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='student_lname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicenquiryform',
            name='student_mname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
