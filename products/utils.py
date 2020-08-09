import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    :param instance:
    :param new_slug:
    :return:
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
