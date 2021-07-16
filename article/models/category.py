from django.db import models
from uuid import uuid4


class Category(models.Model):
    """ 商品のカテゴリ """
    id = models.CharField(max_length=255, default=uuid4, primary_key=True, editable=False)
    category = models.CharField('カテゴリ', max_length=20)

    def __str__(self):
        return f'{self.id} : {self.category}'
