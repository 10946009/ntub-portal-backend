from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    db_ip = models.CharField(max_length=20)
    detail = models.TextField()
    promotor = models.CharField(max_length=100)
    promotor_email = models.EmailField()
    

    def __str__(self):
        return f'{self.name}'