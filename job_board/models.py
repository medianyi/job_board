from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db
# attrs are the fields in the table

# Job posting tablet
## title, description, company, salary

class JobPosting(models.Model):
    title = models.CharField(max_lenght=100)
    description = models.TextField()
    company = models.CharField(max_lenght=100)
    salary = models.IntegerField()


