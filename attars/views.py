from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
from .models import attar
def Attar(request):
    attars=attar.objects.all()
    paginator=Paginator(attars,6)
    page=request.GET.get('page')
    page_attars=paginator.get_page(page)
    context={
        'attars':page_attars
    } 
    return render(request, 'pages/attar.html',context)

def attarss(request, attarss_id):
    attarss=get_object_or_404(attar, pk=attarss_id)
    context = {
     'attarss':attarss
    }
    return render(request, 'pages/attarsingle.html',context)
