from django.shortcuts import  get_object_or_404,render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
from .models import floral
def Floral(request):
    florals=floral.objects.all()
    paginator=Paginator(florals,6)
    page=request.GET.get('page')
    page_florals=paginator.get_page(page)
    context={
        'florals':page_florals
    } 
    return render(request, 'pages/floural.html',context)

def floralss(request, floral_id):
    floralss=get_object_or_404(floral, pk=floral_id)
    context = {
     'floralss':floralss
    }
    return render(request, 'pages/floralsingle.html',context)