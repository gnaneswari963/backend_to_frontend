from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='Iam assuming this data'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)

def login(request):
    d={'username':'Gnaneswari'}
    return render(request,'login.html',context=d)

def register(request):
    d={'name':'Gnanam'}
    return render(request,'register.html',context=d)