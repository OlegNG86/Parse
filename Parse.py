import time

from bs4 import BeautifulSoup as bs
import requests


url = 'http://sro-mosk.ru/reestr/v/58'

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

base_url = 'https://spb.hh.ru/search/vacancy?L_is_autosearch=false&area=2&clusters=true&enable_snippets=true&text=Python&page='

def hh_parse(base_url):
    print(time.clock())
    for Page in range(51):
        print('Страница №: ', Page)



        jobs = []
        session = requests.Session()
        r = session.get(base_url + str(Page), headers=headers)
        soup = bs(r.content, 'lxml')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        TotalPage = soup.find_all('a', attrs={'data-page'})
        print(TotalPage)
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            text_responsibility = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            text_requirement = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text


            # try:
            #     work_schedule = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-work-schedule'}).text
            #     if work_schedule == None:
            #         return None
            #     else:
            #         return work_schedule
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'text_responsibility': text_responsibility,
                'text_requirement': text_requirement
            })

        for i in jobs:
            print(i)
        print(time.clock())


def changePage(url):
    pass


#def get_html(url):


    # r = requests.get(url)
    # html = r.content
    # soup = bs(html)
    # test = soup.find_all(class_='table table-bordered')[0].get_text()
    #
    #
    # print(test)
    #
    #


def main():
    hh_parse(base_url)

if __name__ == '__main__':
    main()
