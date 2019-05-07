from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

from .models import aroma
def Aroma(request):
    aromas=aroma.objects.all()
    paginator=Paginator(aromas,6)
    page=request.GET.get('page')
    page_aroma=paginator.get_page(page)
    context={
        'aromas':page_aroma
    } 
    return render(request, 'pages/aroma.html',context)

def ass(request, ass_id):
    ass=get_object_or_404(aroma, pk=ass_id)
    context = {
     'ass':ass
    }
    return render(request, 'pages/asssingle.html',context)
