from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatRoom

def index(request):
    return render(request, 'chat/index.html', {})

def room(request,room_name,user):
    agent = ChatRoom.send_user_agent(room_name,user)
    if agent:
        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'user_agent':agent
        })
    return redirect("index")

@csrf_exempt
def set_room(request):
    room = request.POST.get("room")
    agent = request.POST.get("agent")
    #if "https://kuboc.rextexh.com/" in request.META['HTTP_HOST'] or "http://127.0.0.1:8000/" in request.META['HTTP_HOST']:
    agent = ChatRoom.send_user_agent(room,agent)
    if agent:
        return JsonResponse({"status":room})
    return JsonResponse({"status":"Not allowed"})