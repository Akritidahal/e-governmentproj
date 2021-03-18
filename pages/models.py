from django.db import models
from address.models import Address
# Create your models here.
class Citizen(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    age=models.IntegerField()
    father_name=models.CharField(max_length=50)
    father_citizen_number=models.CharField(max_length=50)
    grand_father_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    address=models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name