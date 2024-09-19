from django.db import models

class Member(models.Model):
  id =  models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)  

class Account(models.Model):
  id =  models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  id_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="accounts")