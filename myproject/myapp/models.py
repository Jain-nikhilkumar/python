from django.db import models

class MyModel(models.Model):
    subject = models.CharField(max_length=100)
    schema_choices = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    select_schema = models.CharField(max_length=50, choices=schema_choices)
    expiry_date = models.DateField()
