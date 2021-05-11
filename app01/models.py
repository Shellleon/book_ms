from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)

    # class Meta:
    #     db_table = "publisher"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.01)
    inventory = models.IntegerField(verbose_name="库存数")
    sale_num = models.IntegerField(verbose_name="卖出数")
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)

    # class Meta:
    #     db_table = "book"


class Author(models.Model):
    name = models.CharField("姓名", max_length=32, null=False)
    book = models.ManyToManyField(to='Book', verbose_name="书名")
    email = models.EmailField("邮箱", default="")

    # class Meta:
    #     db_table = "author"
