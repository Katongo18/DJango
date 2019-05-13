from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # date_posted = model.models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # enables django to find the location of a specific post
       return reverse("post-detail", kwargs={"pk": self.pk})  # reverse returns the full url o the path as a string