from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Menu
from .forms import CreateForm
from django.db.models import Sum,Count

# Create your views here.
def index(request):
    dates = Menu.objects.all().dates('date','day',order='DESC')
    dateList = []
    calorieList = []
    for date in dates:
        dayCalorie = Menu.objects.filter(date=date).aggregate(Sum('calorie'))
        dateList.append([date,dayCalorie])
    lens = len(dateList)
    params = {
        'posts':Menu.objects.filter(date__lte=timezone.now()).order_by('date').reverse(),
        'dateList':dateList,
    }
    return render(request,'crud/index.html',params)
    
def create(request):
    form = CreateForm()
    return render(request,'crud/create.html',{'form':form})

def form(request):
    if request.method == 'POST':
        menu = request.POST['menu']
        calorie = request.POST['calorie']
        date = request.POST['date']
        
        menu_data = Menu(menu=menu,calorie=calorie,date=date)
        menu_data.save()
        return redirect('index')
    return render(request,'crud/create.html',{'form':form})

def edit(request,id):
    obj = Menu.objects.get(id=id)
    init_dict = {
        'menu':obj.menu,
        'calorie':obj.calorie,
        'date':obj.date,
    }
    params = {
        'post':get_object_or_404(Menu,id=id),
        'form':CreateForm(request.POST or None, initial=init_dict),
    }
    return render(request,'crud/edit.html',params)
    
def update(request,id):
    obj = Menu.objects.get(id=id)
    if request.method == "POST":
        obj.menu = request.POST['menu']
        obj.calorie = request.POST['calorie']
        obj.date = request.POST['date']
        
        obj.save()
        return redirect('index')
    params = {
        'post':get_object_or_404(Menu,id=id),
        'form':CreateForm(),
    }
    return render(request,'crud/edit.html',params)

def delete(request,id):
    obj = Menu.objects.get(id=id)
    obj.delete()
    return redirect('index')
    
def detail(request,id):
    post = Menu.objects.get(id=id)
    return render(request,'crud/detail.html',{'post':post})
        