from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()


    def only_date(self):
        return self.pub_date.strftime('%b %e, %Y')

    def summary(self):
        return self.body[:300]