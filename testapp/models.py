from django.db import models

class hydjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class bangalorejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class chennaijobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class punejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()


