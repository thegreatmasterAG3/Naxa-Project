# Generated by Django 4.1.3 on 2023-03-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('project_title', models.CharField(max_length=100)),
                ('project_status', models.CharField(max_length=100)),
                ('donor', models.CharField(max_length=100)),
                ('executing_agency', models.CharField(max_length=100)),
                ('implementing_partner', models.CharField(max_length=100)),
                ('counterpart_ministry', models.CharField(max_length=100)),
                ('type_of_assistance', models.CharField(max_length=100)),
                ('budget_type', models.CharField(max_length=100)),
                ('humanitarian', models.BooleanField(default=False)),
                ('sector', models.CharField(max_length=100)),
                ('agreement_date', models.DateField(blank=True, null=True)),
                ('commitments', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('dibursement', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
    ]
