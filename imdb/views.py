from django.shortcuts import render


def home(request):
	return render(request, 'home.html' )


def yazboz(request):
    context = { 'iteration':range(1,39)}


    return render(request, 'yazboz.html', context)
