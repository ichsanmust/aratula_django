from django.db import models

# Create your models here.
class Roles(models.Model):
    role_id = models.BigIntegerField(primary_key=True)
    role_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'
        
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    role_0 = models.ForeignKey(Roles, models.DO_NOTHING, db_column='role_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'users'