from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))



def bus_stations(request):
    with open("data-398-2018-08-30.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        bus_stations = []
        for row in file_reader:
            bus_stations.append(row)

    paginator = Paginator(bus_stations, 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)

