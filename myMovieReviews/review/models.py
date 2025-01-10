from django.db import models

# Create your models here.

#아래는 다 수정

class Review(models.Model):
    title = models.TextField()
    release_year = models.TextField()
    director = models.TextField()
    cast = models.TextField()
    genre = models.TextField()
    rating = models.TextField()
    running_time = models.TextField()
    review_content = models.TextField()