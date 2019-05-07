from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

from .models import essential
def Essential(request):
    essentials=essential.objects.all()
    paginator=Paginator(essentials,6)
    page=request.GET.get('page')
    page_essential=paginator.get_page(page)
    context={
        'essentials':page_essential
    } 
    return render(request, 'pages/essential.html',context)

def search(request):
    return render(request, 'pages/search.html')

def ess(request, ess_id):
    ess=get_object_or_404(essential, pk=ess_id)
    context = {
     'ess':ess
    }
    return render(request, 'pages/esssingle.html',context)

