from django.shortcuts import render
from django.http import JsonResponse
from .services import vk_parser
def app(request):
    pars1 = vk_parser.Vk_parser('#photo')
    photos = pars1.get_photo_storage()
    print('===========================================')
    for photo in photos:
        print(photo)
    print('===========================================')

    return JsonResponse({'success': True})
