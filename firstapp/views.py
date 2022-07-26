from datetime import date
import json
from django.http import Http404
import requests
from .models import Publication, Comment, User, Subcomment
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.core.mail import send_mail

from website.settings import EMAIL_HOST_USER


def email(request):
    if request.method == "POST":
        email_address = request.POST['email']
        text = """Hey!\nI'm so glad you're here!\nThanks so much for your support—it means the world to us!\nAll the best! """
        send_mail(
            'Welcome Email',
            text,
            EMAIL_HOST_USER,
            [email_address])
        return render(request, "firstapp/index.html")


def recent_news():
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    recent_objects = Publication.objects.filter(
        date_created__gte=date_from)
    return recent_objects


def category(request, section):
    dict = {
        "politics": "Политика",
        "economics": "Экономика",
        "sports": "Спорт",
        "technology": "Технология",
        "culture": "Культура",
        "community": "Общество",
        "global": "В мире",
    }

    for key, value in dict.items():
        if key == section:
            objects = Publication.objects.filter(section=value).order_by('-id')
            obj_num = objects.count()

    page = request.GET.get("page")
    paginator = Paginator(objects, 9)

    try:
        pubs = paginator.page(page)
    except PageNotAnInteger:
        pubs = paginator.page(1)
    except EmptyPage:
        pubs = paginator.page(paginator.num_pages)

    obj_divided = int(obj_num / 5)

    return render(request, "firstapp/category.html", {
        "pubs": pubs,
        "objects": objects,
        "section": value,
        "obj_num": obj_num,
        "obj_divided": range(obj_divided),
        # "usd_to_sum": converter("USD"),
        # "eur_to_sum": converter("EUR"),
        # "rub_to_sum": converter("RUB"),
        "recent_news": recent_news(),
    })


def contact(request):
    return render(request, "firstapp/contact.html", {
        # "usd_to_sum": converter("USD"),
        # "eur_to_sum": converter("EUR"),
        # "rub_to_sum": converter("RUB"),

        # "weather": weather("Tashkent"),
    })


def index(request):
    objects = Publication.objects.all().order_by('-id')

    topic_list = ["politics", "economics", "sports",
                  "technology", "culture", "community", "global"]
    search_list = ["Политика", "Экономика", "Спорт",
                   "Технология", "Культура", "Общество", "В мире"]

    for i in range(7):
        topic_list[i] = Publication.objects.filter(
            section=search_list[i]).order_by('-id')

    return render(request, "firstapp/index.html",
                  {
                      #   "usd_to_sum": converter("USD"),
                      #   "eur_to_sum": converter("EUR"),
                      #   "rub_to_sum": converter("RUB"),

                      "objects": objects,
                      "politics_objects": topic_list[0],
                      "economy_objects": topic_list[1],
                      "sports_objects": topic_list[2],
                      "tech_objects": topic_list[3],
                      "culture_objects": topic_list[4],
                      "community_objects": topic_list[5],
                      "world_objects": topic_list[6],

                      "recent_news": recent_news(),
                      #   "weather": weather("Tashkent"),
                  })


def view(request, id):
    object = Publication.objects.get(pk=id)
    comments = Comment.objects.filter(publication=object.id)
    pubs_list = [comment.publication for comment in comments]
    subcomments = Subcomment.objects.filter(
        base_comment__publication__in=pubs_list)

    try:
        previous_object = get_object_or_404(Publication, pk=object.id-1)
    except Http404:
        previous_object = None

    try:
        next_object = get_object_or_404(Publication, pk=object.id+1)
    except:
        next_object = None

    return render(request, 'firstapp/view.html',
                  {
                      "object": object,
                      "next_object": next_object,
                      "previous_object": previous_object,
                      "comments": comments,
                      "subcomments": subcomments,
                      #   "recent_news": recent_news(),
                      #   "usd_to_sum": converter("USD"),
                      #   "eur_to_sum": converter("EUR"),
                      #   "rub_to_sum": converter("RUB"),
                  })


# def converter(international_currency):
#     url = f"https://cbu.uz/ru/arkhiv-kursov-valyut/json/{international_currency}/{date.today()}/"
#     response = requests.request("GET", url)
#     json_file = json.loads(response.text)
#     return json_file[0]['Rate']


# def weather(city):
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?appid=eb8083d38c634a3b0fe5efd72449ee98&q={city}"
#     response = requests.get(base_url)
#     x = response.json()
#     return round((x["main"]["temp"] - 273.15))


def search(request):
    my_query = request.GET.get("q")
    page = request.GET.get("page")

    objects_list = Publication.objects.filter(
        Q(title__icontains=my_query) | Q(paragraph1__icontains=my_query) | Q(paragraph2__icontains=my_query) | Q(
            paragraph3__icontains=my_query) | Q(paragraph4__icontains=my_query) | Q(paragraph5__icontains=my_query) | Q(section__iexact=my_query)
    ).order_by('-id').distinct()
    obj_num = objects_list.count()

    paginator = Paginator(objects_list, 5)

    try:
        pubs = paginator.page(page)
    except PageNotAnInteger:
        pubs = paginator.page(1)
    except EmptyPage:
        pubs = paginator.page(paginator.num_pages)

    return render(request, "firstapp/search.html",
                  {
                      #   "usd_to_sum": converter("USD"),
                      #   "eur_to_sum": converter("EUR"),
                      #   "rub_to_sum": converter("RUB"),

                      "search": my_query,
                      "num_of_pubs": obj_num,
                      "pubs": pubs,
                  })
