# Generated by Django 3.1 on 2021-07-15 17:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import uuid
import validation.image_validators


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='article_thumbnail/', validators=[validation.image_validators.image_validator], verbose_name='サムネイル')),
                ('encoded_thumbnail', models.TextField(blank=True, null=True, verbose_name='エンコードしたサムネイル')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('body', models.TextField(verbose_name='本文')),
                ('material', models.TextField(verbose_name='材料')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='article.category', verbose_name='カテゴリ')),
            ],
        ),
    ]