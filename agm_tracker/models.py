from django.db import models

class agm(models.Model):
    codename = models.CharField(max_length=100)
    ticker = models.CharField(max_length=100)
    fund = models.CharField(max_length=100)
    position_name = models.CharField(max_length=100)
    agm_date = models.DateField()
    agm_record = models.DateField()

    def __str__(self):
        return "%s" % (self.codename)

