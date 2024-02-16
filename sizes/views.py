from django.shortcuts import render
from art.settings import STATIC_ROOT


STATIC_ROOT = STATIC_ROOT.replace("\\", "/")

page_title_list = [
    ["МШК-01", "art01"],
    ["МШК-04", "art04"],
    ["МШК-06", "art06"],

]





def art01(request):
    current_page_title = "МШК-01"
    return render(request, 'art01.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def art04(request):
    current_page_title = "МШК-04"
    return render(request, 'art04.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })


def art06(request):
    current_page_title = "МШК-06"
    return render(request, 'art06.html', {
        'current_page_title': current_page_title,
        'page_title_list': page_title_list,
    })





