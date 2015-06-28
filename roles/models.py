from django.db import models

# Create your models here.
class role(models.Model):
    affiliations = (('T', 'Town'),
                    ('M', 'Mafia'),)
    roleName = models.CharField(max_length=15)
    aff = models.CharField(max_length=15, choices=affiliations)
    meetingGroup = models.IntegerField()
    def __unicode__(self):
        return self.roleName

class setup(models.Model):
    setupName = models.CharField(max_length=15)
#   numRoles = models.IntegerField()
    roles = models.ManyToManyField(role, through="roleAdd")

class roleAdd(models.Model):
    role = models.ForeignKey(role)
    setup = models.ForeignKey(setup)
    number = models.IntegerField()
