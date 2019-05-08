from django.shortcuts import get_object_or_404, render
# Create your views here.

from .models import fp
def fpsss(request, fps_id):
    fps=get_object_or_404(fp, pk=fps_id)
    context = {
     'fps':fps
    }
    return render(request, 'pages/fpssingle.html',context)
