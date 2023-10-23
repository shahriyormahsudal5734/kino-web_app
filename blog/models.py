from django.db import models
class Kinolar(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField()
    kino_yili=models.IntegerField()
    nechaminut=models.IntegerField()
    sifati=models.CharField(max_length=50)
    def __str__(self):
        return self.title

    



class Qoshiqlar(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    file = models.FileField(upload_to='static/upload/', blank=True)
    muzicname = models.CharField(max_length=200)



class Bloglar(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    blog = models.CharField(max_length=200)

