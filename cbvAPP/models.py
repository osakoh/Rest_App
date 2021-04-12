from django.db import models


class Student(models.Model):
    # id = models.IntegerField(primary_key=True)  # make the id the primary key
    name = models.CharField(max_length=25)
    score = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.name}"
