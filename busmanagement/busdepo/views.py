from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import render,redirect,get_object_or_404
from busdepo import views
from .forms import DriverForm,BusForm
from .models import Bus

# Create your vi

# Create your views here.
def driver(request):
    if request.method=="POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = DriverForm()
    return render(request,'driver.html',{'form':form})


def bus_list(request):
    buses = Bus.objects.all().order_by("busnumber")
    paginator = Paginator(buses,5)
    page_number = request.GET.get('page')
    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(page_number.num_page)
    return render(request,'bus_list.html',{'buses':buses,'page':page})
def bus_add(request):
    if request.method=="POST":
        form = BusForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = BusForm()
    return render(request,'bus_add.html',{'form':form})


def bus_delete(request, pk):
    bus = get_object_or_404(Bus,pk=pk)
    if request.method=='POST':
            bus.delete()
            return redirect('bus_list')
    return render(request,'bus_delete.html',{'bus':bus})



def bus_update(request, pk):
    bus= get_object_or_404(Bus, pk=pk)
    print(bus)
    if request.method == 'POST':
        form = BusForm(request.POST,request.FILES,instance=bus)  # Support file uploads
        if form.is_valid():
            form.save()
        return redirect('/list')  
    else:
        form = BusForm(instance=bus)
    return render(request, 'bus_update.html', {'form': form})





