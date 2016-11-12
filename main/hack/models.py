from django.db import models
# Create your models here.
class Wisdom(models.Model):
    title = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=10,decimal_places=7)
    latitude = models.DecimalField(max_digits=10,decimal_places=7)
    start = models.DateTimeField()
    end = models.DateTimeField()
    rates = 0
    rating = 0
    categories = []
    """ Include User """
    comment_list = []

    def __str__ (self):
        return self.title

    def add_comment(self, comment):
        self.comment_list.append(comment)

class Tip(Wisdom):
    text = models.CharField(max_length=150)

class Hack(Wisdom):
    text = models.TextField()
    picture = models.ImageField()

class Comment(models.Model):
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
