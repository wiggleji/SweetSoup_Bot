# sweetsoup_cafe.py

import requests
from bs4 import BeautifulSoup as bs
import datetime
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

# jukjeon 555 56 57
# cheonan 560 61 62


# find day of the week
def get_day():
    today = str(datetime.date.today().day)
    today_num = 0
    compare_days = []
    # only get day (ex: 2018-02-12 -> 12)
    print(f"Today : {today}")

    # get dates to compare
    html = requests.get('http://www.dankook.ac.kr/web/kor/-555', headers=headers).text
    soup = bs(html, 'lxml')

    # check day
    days = soup.select('#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr > td > label > span.name_date')
    for i in days:
        compare_days.append(i.text.strip())
    print(compare_days)

    # find today as num, EX: 1 - Monday, 6 - Saturday
    for num, day in enumerate(compare_days, start=1):
        print(num, day)
        which_day = day.find(today)
        if which_day > 0:
            today_num = num
    return today_num

# Crawler for each campus
# work same on different page (juk - 555~57, chn - 560~62)


# Jukjeon Campus
def juk_kyo_menu():
    # list for return value
    result = []
    # get the date from get_day()
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    # parse data from each page ('http://www.dankook.ac.kr/web/kor/{juk, chn}')
    html = requests.get(f'http://www.dankook.ac.kr/web/kor/-555', headers=headers).text
    soup = bs(html, 'lxml')
    # select cafeteria
    cafe = soup.select(
        'div.portlet-borderless-container > div > div > ul > li.on > a > span')
    # select menu with date
    menu = soup.select(
        f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today_as_number}) > td:nth-of-type(2)')
    print(cafe)
    print(menu)

    # append both to result
    cafe_name = cafe[0].text.strip()
    menu_name = menu[0].text.strip().replace(")", ")\n\n").replace("0원","0원\n\n").replace("*", "\n\n*")
    result.append(cafe_name)
    result.append(menu_name)
    print(result)

    return ''.join(result)


def juk_hak_menu():
    result = []
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    html = requests.get(f'http://www.dankook.ac.kr/web/kor/-556', headers=headers).text
    soup = bs(html, 'lxml')
    cafe = soup.select(
        'div.portlet-borderless-container > div > div > ul > li.on > a > span')
    menu = soup.select(
        f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today_as_number}) > td:nth-of-type(2)')
    print(cafe)
    print(menu)

    cafe_name = cafe[0].text.strip()
    menu_name = menu[0].text.strip().replace(")", ")\n\n").replace("0원","0원\n\n").replace("*", "\n\n*")
    result.append(cafe_name)
    result.append(menu_name)
    print(result)

    return ''.join(result)


def juk_sang_menu():
    result = []
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    html = requests.get(f'http://www.dankook.ac.kr/web/kor/-557', headers=headers).text
    soup = bs(html, 'lxml')
    cafe = soup.select(
        'div.portlet-borderless-container > div > div > ul > li.on > a > span')
    menu = soup.select(
        f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today_as_number}) > td:nth-of-type(2)')
    print(cafe)
    print(menu)

    cafe_name = cafe[0].text.strip()
    menu_name = menu[0].text.strip().replace(")", ")\n\n").replace("0원","0원\n\n").replace("*", "\n\n*")
    result.append(cafe_name)
    result.append(menu_name)
    print(result)

    return ''.join(result)


# Cheonan Campus
def chn_kyo_menu():
    result = []
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    html = requests.get(f'http://www.dankook.ac.kr/web/kor/-560', headers=headers).text
    soup = bs(html, 'lxml')
    cafe = soup.select(
        'div.portlet-borderless-container > div > div > ul > li.on > a > span')
    menu = soup.select(
        f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today_as_number}) > td:nth-of-type(2)')
    print(cafe)
    print(menu)

    cafe_name = cafe[0].text.strip()
    menu_name = menu[0].text.strip().replace(")", ")\n\n").replace("0원","0원\n\n").replace("*", "\n\n*")
    result.append(cafe_name)
    result.append(menu_name)
    print(result)

    return ''.join(result)


def chn_hak_menu():
    result = []
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    html = requests.get(f'http://www.dankook.ac.kr/web/kor/-561', headers=headers).text
    soup = bs(html, 'lxml')
    cafe = soup.select(
        'div.portlet-borderless-container > div > div > ul > li.on > a > span')
    menu = soup.select(
        f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today_as_number}) > td:nth-of-type(2)')
    print(cafe)
    print(menu)

    cafe_name = cafe[0].text.strip()
    menu_name = menu[0].text.strip().replace(")", ")\n\n").replace("0원","0원\n\n").replace("*", "\n\n*")
    result.append(cafe_name)
    result.append(menu_name)
    print(result)

    return ''.join(result)


def chn_danhol_menu():
    result = []
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    html = requests.get(f'http://www.dankook.ac.kr/web/kor/-562', headers=headers).text
    soup = bs(html, 'lxml')
    cafe = soup.select(
        'div.portlet-borderless-container > div > div > ul > li.on > a > span')
    menu = soup.select(
        f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today_as_number}) > td:nth-of-type(2)')
    print(cafe)
    print(menu)

    cafe_name = cafe[0].text.strip()
    menu_name = menu[0].text.strip().replace(")", ")\n\n").replace("0원","0원\n\n").replace("*", "\n\n*")
    result.append(cafe_name)
    result.append(menu_name)
    print(result)

    return ''.join(result)


# Start crawling Dankook Univ. Menu in local testing
if __name__ == "__main__":
    print("Testing...")
    # juk_hak_menu()
    # juk_kyo_menu()
    # juk_sang_menu()
    # chn_kyo_menu()
    # chn_hak_menu()
    # chn_danhol_menu()