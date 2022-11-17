from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.model_mixins import StrFromFieldMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image

UserModel = get_user_model()


class Photo(StrFromFieldMixin, models.Model):
    str_fields = ('photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        null=False,
        blank=True,
        validators=(validate_image,),
    )
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,

    )

    publication_date = models.DateField(
        auto_now=True,
        blank=True,
        null=False,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
