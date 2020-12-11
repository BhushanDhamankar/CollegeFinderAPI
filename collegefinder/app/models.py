from django.db import models
class Branch(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default =True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Branches" 

class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default =True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"

class College(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    address = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural="Colleges"

    def __str__(self):
        return self.name


class Mapping(models.Model):
    collegeid = models.ForeignKey(College, on_delete=models.CASCADE)
    branchid = models.IntegerField()
    categoryid = models.IntegerField()
    rank = models.IntegerField()


class model_feedback(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    feed = models.TextField(max_length=500)

 #ForeignKey(College, on_delete=models.CASCADE)