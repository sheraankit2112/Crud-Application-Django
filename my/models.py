from django.db import models

class studentdata(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,unique=True)

    def __str__(self):
        return str(self.id)


