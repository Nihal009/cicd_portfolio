from django.shortcuts import render,get_object_or_404
from .models import bio,projects


def home(request):
    _bio=bio.objects.get()
    # _projects=get_object_or_404()
    context={'bio':_bio}
    return render(request,'home.html',context=context)