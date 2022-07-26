from django.db import models
from django_countries.fields import CountryField


class Publication(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    title_photo = models.ImageField(upload_to="images/")
    section = models.CharField(choices=[
        ("Политика", "Политика"),
        ("Экономика", "Экономика"),
        ("Общество", "Общество"),
        ("Культура", "Культура"),
        ("Спорт", "Спорт"),
        ("В мире", "В мире"),
        ("Технология", "Технология"),
    ], max_length=100, blank=False)
    preview = models.CharField(max_length=100, blank=True)

    paragraph1 = models.CharField(max_length=10000,  blank=True)
    paragraph2 = models.CharField(max_length=10000,  blank=True)
    paragraph3 = models.CharField(max_length=10000,  blank=True)
    paragraph4 = models.CharField(max_length=10000,  blank=True)
    paragraph5 = models.CharField(max_length=10000,  blank=True)

    photo1 = models.ImageField(upload_to="firstapp/static/img",  blank=True)
    photo2 = models.ImageField(upload_to="firstapp/static/img",  blank=True)
    photo3 = models.ImageField(upload_to="firstapp/static/img",  blank=True)
    photo4 = models.ImageField(upload_to="firstapp/static/img",  blank=True)
    photo5 = models.ImageField(upload_to="firstapp/static/img",  blank=True)

    tag1 = models.CharField(max_length=20, blank=True)
    tag2 = models.CharField(max_length=20, blank=True)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    tag5 = models.CharField(max_length=20, blank=True)


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(
        upload_to="images/profile_picture", default="profile_picture/default.jpg")
    email = models.EmailField(max_length=254, unique=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    country_origin = CountryField()

    def __str__(self):
        return f"{ self.username }"


class Comment(models.Model):
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{ self.body }"


class Subcomment(models.Model):
    base_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{ self.body }"
