from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'Lets learn Java'},
#     {'id':3, 'name':'Lets learn python'},
# ]

# 設定主頁面
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

# 設定每個房間頁面
def room(request,pk):
    room =Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)

# 設定新增房間頁面
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request,'base/room_form.html',context)

# 設定更新房間頁面
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' :form}
    return render(request,'base/room_form.html',context)

# 設定刪除房間頁面
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})
