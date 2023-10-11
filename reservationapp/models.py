from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


# Create your models here.
class Reservation(models.Model):
    Firstname=models.CharField(max_length=80,blank=False,null=False)
    Lastname=models.CharField(max_length=80,blank=False,null=False)
    Email=models.EmailField(blank=False,null=False)
    Phone=models.CharField(max_length=80,blank=False,null=False)
    Address=models.CharField(max_length=80,blank=False,null=False)
    Address2=models.CharField(max_length=80,blank=True,null=True)
    Zip_code=models.CharField(max_length=6,blank=False,null=False)
    State=models.CharField(max_length=80,blank=False,null=False)
    Image=models.FileField(upload_to="media",blank=False,null=False)
    Date_checkIn=models.DateField(blank=False,null=False)
    Time_checkIn=models.TimeField(blank=False,null=False)
    Date_checkOut=models.DateField(blank=False,null=False)
    Time_checkOut=models.TimeField(blank=False,null=False)




    def __str__(self):
        return self.Firstname + " " + self.Lastname

    def clean(self):
    # Check the date fields to make sure that they are valid.
        today = date.today()
        if self.Date_checkIn < today:
            raise ValidationError('The check-in date cannot be in the past.')
        if self.Date_checkOut < self.Date_checkIn:
            raise ValidationError('The check-out date cannot be earlier than the check-in date.')

