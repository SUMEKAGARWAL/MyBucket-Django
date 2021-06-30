from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from home.models import Task
from django.contrib import messages
from .forms import TaskForm


# Create your views here.
def home(request):
    context = {'success':False}
    if request.method == "POST":
        #handle the form dude
        print("mere kana aagaya eenuuu")
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context = {'success':True}
    return render(request, 'index.html',context)


def task(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks} 
    return render(request, 'task.html',context) 

def delete_contact(request, pk):
    curr_contact = Task.objects.get(id=pk)
    if request.method == "POST":
        curr_contact.delete()
        # messages.error(request, "deleted successfully!!")  # this was getting printed on the admin site with a red mark which was daunting
        return redirect('/task')
    print("selected NO")
    context = {'item': curr_contact}
    return render(request, 'delete_contact.html', context)


def Update_contact(request, pk):
    curr_contact = Task.objects.get(id = pk)
    print(curr_contact.taskDesc)
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        Task.objects.filter(id = pk).update(taskTitle=title)
        Task.objects.filter(id = pk).update(taskDesc=desc)
        return redirect('/task')
    context = {"sayid": curr_contact.id, "saytitle" : curr_contact.taskTitle , "saydesc": curr_contact.taskDesc}
    return render(request, 'newupdate.html',context)


#def Update_contact(request, pk):
#    obj = get_object_or_404(Task,id = pk)
#    form = TaskForm(request.POST or None, instance = obj)
#    if(form.is_valid()):
#        form.save()
#        return redirect('/task')
#    print("its going")
#    context = {'item': form}
#    return render(request, 'newupdate.html',context)


def chatbot(request):
    return render(request,'chatty.html')