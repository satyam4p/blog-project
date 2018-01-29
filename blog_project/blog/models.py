from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.

class post(models.Model):
    author=models.ForeignKey('auth.User')
    text=models.TextField()
    title=models.CharField(max_length=200)
    create_time=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(null=True,blank=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)
    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={'pk':self.pk})
    def __str__(self):
        return self.title


class comments(models.Model):
    post=models.ForeignKey('blog.post',related_name='comments')
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    approved_comment =models.BooleanField(default=False)


    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text



