from django.db import models

# Create your models here.
class Company(models.Model):
    eno = models.IntegerField();
    ename = models.CharField(max_length=30);
    esal = models.FloatField();
    eaddr = models.CharField(max_length=30);


from django.db import models
# Create your models here.
class Company(models.Model):
    eno=models.IntegerField();
    ename=models.CharField(max_length=30);
    esal=models.FloatField();
    eaddr=models.CharField(max_length=30);
    def __str__(self):
        return 'Employee Object with eno: '+str(self.eno);

