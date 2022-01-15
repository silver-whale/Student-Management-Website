from django.db import models

class Students(models.Model):
    id_num = models.IntegerField(db_column='ID_num', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondname = models.CharField(db_column='Secondname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='Major', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'students'