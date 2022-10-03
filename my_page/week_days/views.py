from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

things_dict = {
    'monday': '1 - Сходить в магазин, 2 - Накормить кота',
    'tuesday': '1 - Подоить корову, 2 - Испечь торт'
}
def get_info_about_todo(request, thing:str):
    data ={
        'year_born': 1974,
        'city_born': 'Пекин',
        'movie_name': 'Константин',
    }
    return render(request, 'week_days/greeting.html', context=data)

def get_info_about_todo_by_number(request, thing: int):
    things = list(things_dict)
    if thing > len(things):
        return HttpResponse('Неверный день!')
    name_of_thing =  things[thing-1]
    redirect_url = reverse('week_days-name', args=(name_of_thing, ))
    return HttpResponseRedirect(redirect_url)
