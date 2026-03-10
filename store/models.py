from django.db import models

#One-to-Many
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"


# Many-to-many
class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self):
        return self.name
