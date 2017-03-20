# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:57
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import Case, Value, When
from temba.utils.models import generate_uuid


def populate_export_status(apps, schema_editor):
    ExportFlowResultsTask = apps.get_model('flows', 'ExportFlowResultsTask')
    ExportFlowResultsTask.objects.update(status=Case(When(is_finished=True, then=Value('C')), default=Value('O')))


def populate_uuid(apps, schema_editor):
    ExportFlowResultsTask = apps.get_model('flows', 'ExportFlowResultsTask')
    for task in ExportFlowResultsTask.objects.filter(uuid=None):
        task.uuid = generate_uuid()
        task.save(update_fields=('uuid',))


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('flows', '0089_baseexporttask_1'),
    ]

    operations = [
        migrations.RunPython(populate_export_status),
        migrations.RunPython(populate_uuid),
        migrations.RemoveField(
            model_name='exportflowresultstask',
            name='is_finished',
        ),
        migrations.AlterField(
            model_name='exportflowresultstask',
            name='uuid',
            field=models.CharField(db_index=True, default=generate_uuid,
                                   help_text='The unique identifier for this object', max_length=36, unique=True,
                                   verbose_name='Unique Identifier'),
        ),
    ]
