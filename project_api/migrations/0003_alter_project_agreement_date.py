# Generated by Django 4.1.3 on 2023-03-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0002_rename_dibursement_project_disbursement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='agreement_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]