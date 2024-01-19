from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db
# attrs are the fields in the table

# Job posting tablet
## title, description, company, salary

class JobPosting(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)


# CRUD
# create
# read
# update
# delete