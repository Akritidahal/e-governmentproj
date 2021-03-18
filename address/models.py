from django.db import models

# Create your models here.
class Address(models.Model):
    zone=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    village=models.CharField(max_length=50)
    ward_no=models.IntegerField()
    tole=models.CharField(max_length=50)
    house_no=models.IntegerField()
    address_type=models.CharField(max_length=50)

    def __str__(self):
        return self.address_type