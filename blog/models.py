from django.db import models
 # declare a new model with a name "BlogModel"
class BlogModel(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title
