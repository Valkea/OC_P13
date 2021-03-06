from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Letting


def index(request):
    """
    Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis
    velit. Sed non placerat massa. Integer est nunc, pulvinar a tempor et,
    bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et
    ultrices posuere cubilia curae; Cras eget scelerisque
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
    porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
    purus urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean
    finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue,
    dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
    potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem
    accumsan interdum. Ut quis urna pellentesque justo mattis ullamcorper ac
    non tellus. In tristique mauris eu velit fermentum, tempus pharetra est
    luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non
    dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
    Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Letting.DoesNotExist:
        return HttpResponseNotFound(f"Letting ID:{letting_id} doesn't exist")


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)
