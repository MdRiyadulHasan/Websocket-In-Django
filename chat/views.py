from django.shortcuts import render
from .models import Group, ChatInfo

# Create your views here.
def index(request, group_name):
    print("Group Name", group_name)
    group = Group.objects.filter(name = group_name).first()
    chats = []
    if group:
        chats = ChatInfo.objects.filter(group= group)

    else:
        Group.objects.create(name = group_name)
    return render(request, 'chat/index.html', {'groupname': group_name, 'chats':chats})
