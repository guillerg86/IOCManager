from django.db import models

class AllowedIP(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField(unique=True)
    short_description = models.CharField(null=True, max_length=40)
    description = models.TextField(null=True)
    created = models.DateTimeField(blank=False,auto_now_add=True)
    modified = models.DateTimeField(blank=False,auto_now_add=True)
    deleted = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.ip

class BlockedIP(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField(unique=False)
    source = models.CharField(max_length=100)
    description = models.TextField(null=True)
    ban_date = models.DateField(null=False)
    ban_expires = models.DateField(null=True,blank=True)
    created = models.DateTimeField(blank=False,auto_now_add=True)
    modified = models.DateTimeField(blank=False,auto_now_add=True)
    deleted = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.ip
