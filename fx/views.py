import cStringIO

from django.http.response import HttpResponse
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvas

from YC301.settings import BASE_DIR
from fx import utils


# Create your views here.
def index(request):
    context={}
    
    return render(request, 'fx/yc301.html', context)

def getgra(request):
    import matplotlib.pyplot as plt
    import numpy as np
    fig=plt.figure()
    plt.plot([1,2,3,4])
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response 
