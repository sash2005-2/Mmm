from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from mmmm.models import Article

# Create your views here.
from django.shortcuts import render_to_response


def main(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'mmmm/index.html', context)


def portpholyo(request):
    return render(request, 'mmmm/portpholyo.html')


def CV(request):
    return render(request, 'mmmm/CV.html')


def aboutMe(request):
    return render(request, 'mmmm/aboutMe.html')


def develop(request):
    return render(request, 'mmmm/develop.html')


def hobby(request):
    return render(request, 'mmmm/hobby.html')


def contact(request):
    return render(request, 'mmmm/contact.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'mmmm/article.html', {'article': article})