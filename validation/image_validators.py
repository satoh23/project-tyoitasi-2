from django.core.exceptions import ValidationError


def image_validator(image):
    """ ファイルの容量制限 """
    if image.size > 4*1024*1024:
        raise ValidationError('画像のサイズが大きすぎます。',
                              params={'image': image},)
