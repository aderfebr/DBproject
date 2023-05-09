# Generated by Django 4.1.7 on 2023-05-04 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_name_area_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='report',
        ),
        migrations.CreateModel(
            name='work_report',
            fields=[
                ('staff_date', models.DateTimeField(primary_key=True, serialize=False)),
                ('report', models.CharField(max_length=200, null=True)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
            options={
                'unique_together': {('area_id', 'staff_id')},
            },
        ),
    ]
