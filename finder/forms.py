from django import forms
from .models import NewsSite
from .models import Category
import datetime


class SearchConditions(forms.Form):
    site_name = forms.ModelChoiceField(
        label='サイト名：',
        empty_label='選択してください',
        queryset=NewsSite.objects.all()
    )

    # TODO: カテゴリは選択したサイトに応じて動的に変化させる
    category_name = forms.ModelChoiceField(
        label='カテゴリ：',
        empty_label='選択してください',
        queryset=Category.objects.all()
    )

    search_word = forms.CharField(
        label='検索ワード：',
        max_length=255
    )

    search_term_start = forms.DateField(
        label='取得期間：',
        initial=datetime.date.today
    )

    search_term_end = forms.DateField(
        initial=datetime.date.today
    )

