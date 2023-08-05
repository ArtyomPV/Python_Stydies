from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(posting=Sum('rating_post'))
        prat = 0
        prat += postRat.get('posting')
        self.rating = prat
        self.save()


