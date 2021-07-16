from uuid import uuid4

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils import timezone

from accounts.models import CustomUser
from article.models import Category
from validation import image_validator


class Detail(models.Model):
    id = models.CharField(max_length=255, default=uuid4, primary_key=True, editable=False)
    thumbnail = ProcessedImageField(
        verbose_name='サムネイル', upload_to='article_thumbnail/', processors=[ResizeToFill(500, 333)],
        format='JPEG', options={'quality': 60}, null=True, blank=True, validators=[image_validator])
    encoded_thumbnail = models.TextField('エンコードしたサムネイル', blank=True, null=True)
    title = models.CharField('タイトル', max_length=50)
    body = models.TextField('本文')
    material = models.TextField('材料')
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    author_id = models.ForeignKey(CustomUser, verbose_name='筆者', on_delete=models.PROTECT)

    created_date = models.DateTimeField('登録日', default=timezone.now)

    def __str__(self):
        return f'{self.title} : {self.created_date}'
