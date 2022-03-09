from django.db import models

class position(models.Model):
    ticker = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    indice = models.CharField(max_length=100)
    shares_issued = models.BigIntegerField(default=0)
    shares_outstanding = models.BigIntegerField(default=0)
    treasury_shares = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return "%s" % (self.company_name)