from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Issues (models.Model):
    issueId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    checkId = models.CharField(max_length=10, blank=True, default='')
    checkDesc = models.CharField(max_length=100, blank=True, default='')
    severity = models.CharField(max_length=1, blank=True, default='')
    issueClientId = models.UUIDField()
    fixStatus = models.CharField(max_length=1, blank=True, default='')
    creationDate = models.DateTimeField(default=timezone.now, blank=True)
    checkComment = models.CharField(max_length=1000, blank=True, default='')


class Users (models.Model):
    userId = models.CharField(max_length=100, blank=True, default='')
    userName = models.CharField(max_length=100, blank=True, default='')
    userPassword = models.CharField(max_length=100, blank=True, default='')
    fullName = models.CharField(max_length=100, blank=True, default='')
    accessLevel = models.CharField(max_length=100, blank=True, default='')
    creationDate = models.CharField(max_length=100, blank=True, default='')
    userPref = models.CharField(max_length=100, blank=True, default='')


class Clients (models.Model):
    clientId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    clientIP = models.CharField(max_length=100, blank=True, default='')
    clientName = models.CharField(max_length=100, blank=True, default='')
    clientPrefs = models.CharField(max_length=100, blank=True, default='')
    clientGroupID = models.CharField(max_length=100, blank=True, default='')


class ClientGroups (models.Model):
    groupID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    groupName = models.CharField(max_length=100, blank=True, default='')
    groupPrefs = models.CharField(max_length=100, blank=True, default='')