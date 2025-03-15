from django.db import models




class ecom(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table="ecom"



class call(models.Model):
    name=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    email=models.EmailField()
    cal=models.DateField()
    class Meta:
        db_table="call"