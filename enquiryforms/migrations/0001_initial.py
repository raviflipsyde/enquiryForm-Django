# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicEnquiryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('enq_date', models.DateTimeField(verbose_name='date published')),
                ('career_choice', models.CharField(max_length=20)),
                ('student_fname', models.CharField(max_length=50)),
                ('student_mname', models.CharField(max_length=50)),
                ('student_lname', models.CharField(max_length=50)),
                ('contact_no_primary', models.CharField(max_length=10)),
                ('contact_no_home', models.CharField(max_length=10)),
                ('contact_email', models.CharField(max_length=100)),
                ('address_home', models.CharField(max_length=1000)),
                ('father_name', models.CharField(max_length=200)),
                ('father_contact_primary', models.CharField(max_length=10)),
                ('father_contact_home', models.CharField(max_length=10)),
                ('ssc_school', models.CharField(max_length=100)),
                ('ssc_classes', models.CharField(max_length=100)),
                ('ssc_science', models.CharField(max_length=6)),
                ('ssc_maths', models.CharField(max_length=6)),
                ('ssc_aggregate', models.CharField(max_length=6)),
                ('ssc_percent', models.CharField(max_length=6)),
            ],
        ),
    ]
