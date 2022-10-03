from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def set_room(request):
    room = request.POST.get("room")
    return JsonResponse({"status":room})