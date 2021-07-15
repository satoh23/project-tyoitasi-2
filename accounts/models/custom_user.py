from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from validation import image_validator


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('メールアドレスは必須です')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff属性をTrueに変更してください')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser属性をTrueに変更してください')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ emailとパスワードでログインする """
    username_validator = UnicodeUsernameValidator()

    id = models.CharField(max_length=255, default=uuid4, primary_key=True, editable=False)
    email = models.EmailField('メールアドレス', unique=True)
    username = models.CharField(
        'ユーザー名', max_length=255, blank=True, default='名無しさん', validators=[username_validator])
    user_profile = models.TextField('プロフィール', max_length=500, blank=True, default='よろしくお願いします')
    user_icon = ProcessedImageField(
        verbose_name='アイコン', upload_to='user_icon/', processors=[ResizeToFill(500, 333)],
        format='JPEG', options={'quality': 60}, null=True, blank=True, validators=[image_validator])
    encoded_icon = models.TextField('エンコードしたアイコン', blank=True, null=True)
    created_date = models.DateTimeField('登録日', default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def email_user(self, subject, message, from_email=None, **kwargs):
        """登録されたemailにメールを送信する"""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f'{self.username} : {self.email}'
