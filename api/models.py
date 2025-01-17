from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    
    address_street = models.CharField(max_length=100)
    address_suite = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_zipcode = models.CharField(max_length=10)
    address_lat = models.FloatField()
    address_lng = models.FloatField()

    phone = models.CharField(max_length=11)
    website = models.URLField()

    company_name = models.CharField(max_length=100)
    company_catchphrase = models.CharField(max_length=100)
    company_bs = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Posts(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
    def __str__(self):
        return self.userId

class Comments(models.Model):
    postId = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email= models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.body

class Albums(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Photos(models.Model):
    albumId = models.ForeignKey(Albums, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    thumbnailUrl = models.URLField(blank=True)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.thumbnailUrl

class Todos(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        if self.completed == True:
            return f"[Realizado] {self.title}"
        else:
            return f"[Não realizado] {self.title}"

