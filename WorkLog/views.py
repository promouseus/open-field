from django.shortcuts import render
from .forms import LogbookForm
#from django.utils import translation


# Create your views here.
def index(request):
    context = {}
    return render(request, 'WorkLog/index.html', context)


def logbook(request):
    if request.method == 'POST':
        f = LogbookForm(request.POST)
        if f.is_valid():
            f.save()
            form = LogbookForm()
            context = {
                'form': form,
            }
            return render(request, 'WorkLog/logbook.html', context)
        else:
            context = {
                'form': f,
            }
    else:
        form = LogbookForm()
        context = {
            'form': form,
        }
    return render(request, 'WorkLog/logbook.html', context)


def language(request):
    context = {
        'redirect_to': '/logbook.html'
    }
    return render(request, 'WorkLog/language.html', context)
