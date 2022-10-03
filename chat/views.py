from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

@csrf_exempt
def set_room(request):
    if "https://kuboc.rextexh.com/" in request.META['HTTP_HOST']:
        room = request.POST.get("room")
    return JsonResponse({"status":room})