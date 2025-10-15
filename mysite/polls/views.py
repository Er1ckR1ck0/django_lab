import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .forms import ArticleForm
from .models import Article

def contact_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.data_published = timezone.now()
            article.save()
            return redirect("/polls/success")
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    return render(request, 'public.html', {'form': form })

def success_view(request):
    return HttpResponse("Success!")


