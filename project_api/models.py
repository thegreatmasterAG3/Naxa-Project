from django.db import models
from datetime import datetime

# Create your models here.

class Project(models.Model):
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    project_title = models.CharField(max_length=100)
    project_status = models.CharField(max_length=100)
    donor = models.CharField(max_length=100)
    executing_agency = models.CharField(max_length=100)
    implementing_partner = models.CharField(max_length=100)
    counterpart_ministry = models.CharField(max_length=100)
    type_of_assistance = models.CharField(max_length=100)
    budget_type = models.CharField(max_length=100)
    humanitarian = models.BooleanField(default=False)
    sector = models.CharField(max_length=100)
    agreement_date = models.CharField(null=True,blank=True, max_length=100)
    commitments = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=True)
    disbursement = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=True)
    

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.project_title