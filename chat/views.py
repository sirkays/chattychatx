from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatRoom

def index(request):
    return render(request, 'chat/index.html', {})


def room(request,room_name):
    chat_room = ChatRoom.get_room(room_name,False)
    if chat_room:
        return render(request, 'chat/room.html', {
            'room_name': chat_room
        })
    return JsonResponse({})

@csrf_exempt
def set_room(request):
    chat_room= None

    #if "https://kuboc.rextexh.com/" in request.META['HTTP_HOST'] or "http://127.0.0.1:8000/" in request.META['HTTP_HOST']:
    chat_room = ChatRoom.get_room(request.POST.get("room"))
    return JsonResponse({"status":chat_room.id})