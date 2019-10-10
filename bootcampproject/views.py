from django.shortcuts import HttpResponse, render


def page(request):
	message = "<h1>salut</h1>"
	return HttpResponse(message)