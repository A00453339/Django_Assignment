from django.db import models


class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200 , null= False)
    price = models.FloatField()
    available = models.CharField(max_length=10)

    def __str__(self):
        return self.name
