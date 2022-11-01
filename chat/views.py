from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatBoxData,Chat
from django.core import serializers
def index(request):
    return render(request, 'chat/index.html', {})

def new(request):
    return render(request, 'chat/new.html', {})

def get_chats(request,user):
    chats = Chat.objects.filter(user=user)
    chats = serializers.serialize('json', chats)
    return JsonResponse({"chats":chats})


def room(request,room,current_user):
    room = ChatBoxData.get_room(room)
    chats = Chat.objects.filter(chat_box=room)
    if room:
        if current_user == room.user1:
            agent = '0'
        else:
            agent = '1'
        return render(request, 'chat/room.html', {
            'room_name': room.room,
            'user_agent':agent,
            "chats":chats,
            "current_user":current_user
            
        })
    return redirect("index")

def chat_user(request,room,current_user):
    room = ChatBoxData.get_room(room)
    chats = Chat.objects.filter(chat_box=room)
    if room:
        if current_user == room.user1:
            agent = '0'
        else:
            agent = '1'
        return render(request, 'chat/message.html', {
            'room_name': room.room,
            'user_agent':agent,
            "chats":chats,
            "current_user":current_user
            
        })
    return redirect("index")


@csrf_exempt
def set_room_mobile(request,room,user1,user2):
    room_name = room
    user = user1
    other_user = user2
    room = ChatBoxData.get_room(room_name)
    if room == False:
        room  =  ChatBoxData.create_room(room_name,user,other_user)
    #if "https://kuboc.rextexh.com/" in request.META['HTTP_HOST'] or "http://127.0.0.1:8000/" in request.META['HTTP_HOST']:
    #agent = ChatRoom.send_user_agent(room,user)
    if room:
        return redirect("chat_user", room=room.room, current_user=user)
    return JsonResponse({"status":"Not allowed"})

@csrf_exempt
def try_now(request):
    return render(request,'chat/message.html')

@csrf_exempt
def set_room(request):
    room_name = request.POST.get("room")
    user = request.POST.get("user")
    other_user = request.POST.get("other_user")
    room = ChatBoxData.get_room(room_name)
    if room == False:
        room  =  ChatBoxData.create_room(room_name,user,other_user)
    #if "https://kuboc.rextexh.com/" in request.META['HTTP_HOST'] or "http://127.0.0.1:8000/" in request.META['HTTP_HOST']:
    #agent = ChatRoom.send_user_agent(room,user)
    if room:
        return JsonResponse({"status":"success","room":room.room})
    return JsonResponse({"status":"Not allowed"})