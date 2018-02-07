from django.shortcuts import render


# Create your views here.
def configuration(request):
    return render(request, 'configuration/configuration.html')


