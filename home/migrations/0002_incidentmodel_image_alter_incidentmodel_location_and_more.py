# Generated by Django 4.1.6 on 2023-04-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentmodel',
            name='image',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='incidentmodel',
            name='location',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='incidentmodel',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incidentmodel',
            name='type',
            field=models.IntegerField(choices=[(0, 'Road Accidents'), (1, 'Domestic Accidents'), (2, 'Industrial Accidents')]),
        ),
    ]
