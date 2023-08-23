from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from chat.models import Group, ChatInfo

# Create your views here.
def index(request, group_name):
    print("Group Name", group_name)
    group = Group.objects.filter(name = group_name).first()
    chats = []
    if group:
        chats = ChatInfo.objects.filter(group= group)

    else:
        Group.objects.create(name = group_name)
    return render(request, 'Practice/index.html', {'groupname': group_name, 'chats':chats})