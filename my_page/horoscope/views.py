from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {
    'aries': 'Знак зодиака Овен',
    'taurus': 'Знак зодиака Телец',
    'gemini': "Знак зодиака Близнецы",
    'cancer': "Знак зодиака Рак",
    'leo': "Знак зодиака Лев",
    'virgo': "Знак зодиака Дева",
    'libra': "Знак зодиака Весы",
    'scorpio': "Знак зодиака Скорпион",
    'sagittarius': "Знак зодиака Стрелец",
    'capricorn': "Знак зодиака Козерог",
    'aquarius': "Знак зодиака Водолей",
    'pisces': "Знак зодиака Рыбы",
}

type_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def index(request):
    zodiacs = list(zodiac_dict)
    # li_element += f"<li> <a href={redirect_url}>{sign.title()}</a></li>"
    context = {
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    sign = sign_zodiac
    context = {
        'description': description,
        'sign_zodiac': sign,
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponse("Неверный порядковый номер зз!")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_info_about_type(request):
    types = list(type_dict)
    li_element = ''
    for t in types:
        redirect_url = reverse("horoscope-element", args=[t])
        li_element += f'<li><a href={redirect_url}>{t.title()}</a></li>'
    response = f'<ol>{li_element}</ol>'
    return HttpResponse(response)


def get_info_about_one_type(request, element: str):
    if element != 'fire' and element != 'water' and element != 'air' and element != 'earth':
        return HttpResponse("Неверная ссылка")
    elements = list(type_dict[element])
    li_element = ""
    for t in elements:
        redirect_url = reverse("horoscope-name", args=[t])
        li_element += f'<li><a href={redirect_url}>{t.title()}</a></li>'
    response = f'<ol>{li_element}</ol>'
    return HttpResponse(response)
