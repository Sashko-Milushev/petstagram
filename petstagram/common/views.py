from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    # TODO: fix this for current user, when authentication is available
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def get_user_liked_photos(photo_id):
    # TODO: fix when have auth
    return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):

    user_liked_photos = get_user_liked_photos(photo_id)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    # Variant 2


    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'

    return redirect(redirect_path)

    # Variant 1 (could be used for update!)
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()

