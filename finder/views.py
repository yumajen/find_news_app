from django.shortcuts import render
from .models import Article
from .forms import SearchConditions


def index(request):
    articles = Article.objects.all()

    # サイト名選択セレクトボックス
    form = SearchConditions(request.POST or None)

    context = {
        'articles': articles,
        'form': form
    }

    return render(request, 'finder/index.html', context)


