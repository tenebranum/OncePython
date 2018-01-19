# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_monthjournal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthjournal',
            options={'verbose_name': 'Month journal', 'verbose_name_plural': 'Month journals'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='Leader'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='group',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(unique_for_month=b'date', verbose_name='Students', to='students.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=b'', max_length=256, verbose_name='Middle name', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='Student ticket'),
        ),
    ]
