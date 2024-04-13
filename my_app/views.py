from django.http import HttpResponse


# Create your views here.
def MyView(request):
    return HttpResponse('Hello, World!')


