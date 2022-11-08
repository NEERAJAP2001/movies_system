from django.db import models
# Create your models here.


class Theatre(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Movies(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    Date_of_release = models.DateField()
    Remaning_tickets = models.IntegerField(default=60)


    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)


class customer1(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)