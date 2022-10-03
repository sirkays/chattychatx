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
    room = request.POST.get("room")
    room2 = request.GET.get("room")
    return JsonResponse({"status":room, "roomw":request.method,"room2":room2})