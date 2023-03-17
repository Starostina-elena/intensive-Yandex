from django.db import models


class Feedback(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
