from django.db import models

class UserModel(models.Model):
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.email
