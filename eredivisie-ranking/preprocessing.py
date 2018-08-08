from bs4 import BeautifulSoup
import requests
import urllib.request
import ast
import time
import pandas as pd


def retrieve_data():

    # gets portal to dutch clubs
    site = requests.get('http://footballdatabase.com/clubs-list-country/netherlands')
    # gets html from site
    content = BeautifulSoup(site.content, 'html.parser')
    # all href's to different clubs
    clubs = content.select('a.sm_logo-name.clubbrowser-club')

    data_points = []

    # for every href do some magic
    for club in clubs:
        club_name = club.get_text()
        print(club_name)
        url = 'http://www.footballdatabase.com' + club.get('href')
        u = urllib.request.urlopen(url)
        data = u.read().decode('utf-8')
        # finds table of data
        table_string = data.split("{startDrawingChart()};var data_array=[['Month','Points','Rank'],")[1].split(';startDrawingChart=function()')[0]
        table_string = '[' + table_string
        
        # converts string of list to proper list
        table = ast.literal_eval(table_string)
        # only appends january and december
        for column in table:

            if 'August' in column[0]:
                score = column[1]
                year = column[0][7:]
                data_points.append((club_name, score, int(year)))


    df = pd.DataFrame(data_points, columns=['club_name', 'tr_begin', 'year'])

    rankings = []

    for i in range(10, 18):

        print("20" + str(i))  
        # since site has no data for 2014 manually added data
        if i == 14:
            
            list = [('PSV Eindhoven', 1, 2014), ('Ajax', 2, 2014), 
                    ('AZ Alkmaar', 3, 2014), ('Feyenoord', 4, 2014), 
                    ('Vitesse', 5, 2014), ('PEC Zwolle', 6, 2014), 
                    ('SC Heerenveen', 7, 2014), ('FC Groningen', 8, 2014), 
                    ('Willem II', 9, 2014), ('FC Twente', 10, 2014), 
                    ('FC Utrecht', 11, 2014), 
                    ('Cambuur', 12, 2014), ('ADO Den Haag', 13, 2014), 
                    ('Heracles', 14, 2014), ('Excelsior', 15, 2014),
                    ('NAC Breda', 16, 2014), ('Go Ahead Eagles', 17, 2014)]
            for tuple in list:
                rankings.append(tuple)
        else:

            url = ('http://footballdatabase.com/league-scores-tables/netherlands-eredivisie-20'
                   + str(i) + '-' + str(i + 1))
            site = requests.get(url)
            content = BeautifulSoup(site.content, 'html.parser')
            table = content.findAll('table')[0]

            year = int('20' + str(i))

            for table_row in table.select('tr'):
                cells = table_row.findAll('td')
                if len(cells) > 0:
                    club_name = cells[1].text.strip()
                    ranking = cells[0].text.strip()
                    rankings.append((club_name, int(ranking), year))
        
    ranking_df = pd.DataFrame(rankings, columns=['club_name', 'ranking', 'year'])
    df = df.merge(ranking_df, on=['club_name', 'year'], how='left')
    
    # remove missing datapoints from dataframe
    df.dropna(how='any', inplace=True)

    # range of possible ranks
    binrange = range(0, 19, 3)
    # ranges of rank_class
    labrange = range(1, 7) 

    # reset ranking to integers
    df.ranking = df.ranking.astype(int)

    df['ranking_class'] = pd.cut(df['ranking'], bins=binrange, labels=labrange)

    df.to_csv('eredivisie-ranking.csv')


def main():

    url = 'https://www.transfermarkt.nl/eredivisie/startseite/wettbewerb/NL1'
    site = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
                                     })
    content = BeautifulSoup(site.content, 'html.parser')
    print(content)

    # # gets portal to dutch clubs
    # site = requests.get('http://footballdatabase.com/clubs-list-country/netherlands')
    # # gets html from site
    # content = BeautifulSoup(site.content, 'html.parser')
    # # all href's to different clubs
    # clubs = content.select('a.sm_logo-name.clubbrowser-club')

    # data_points = []

    # # for every href do some magic
    # for club in clubs:
    #     club_name = club.get_text()
    #     print(club_name)
    #     url = 'http://www.footballdatabase.com' + club.get('href')
    #     u = urllib.request.urlopen(url)
    #     data = u.read().decode('utf-8')
    #     # finds table of data
    #     table_string = data.split("{startDrawingChart()};var data_array=[['Month','Points','Rank'],")[1].split(';startDrawingChart=function()')[0]
    #     table_string = '[' + table_string
        
    #     # converts string of list to proper list
    #     table = ast.literal_eval(table_string)
    #     # only appends january and december
    #     for column in table:

    #         if 'August' in column[0]:
    #             score = column[1]
    #             year = column[0][7:]
    #             data_points.append((club_name, score, int(year)))

    # rankings = []

    # for i in range(10, 18):

    #     print("20" + str(i))  
    #     # since site has no data for 2014 manually added data
    #     if i == 14:
            
    #         list = [('PSV Eindhoven', 1, 2014), ('Ajax', 2, 2014), 
    #                 ('AZ Alkmaar', 3, 2014), ('Feyenoord', 4, 2014), 
    #                 ('Vitesse', 5, 2014), ('PEC Zwolle', 6, 2014), 
    #                 ('SC Heerenveen', 7, 2014), ('FC Groningen', 8, 2014), 
    #                 ('Willem II', 9, 2014), ('FC Twente', 10, 2014), 
    #                 ('FC Utrecht', 11, 2014), 
    #                 ('Cambuur', 12, 2014), ('ADO Den Haag', 13, 2014), 
    #                 ('Heracles', 14, 2014), ('Excelsior', 15, 2014),
    #                 ('NAC Breda', 16, 2014), ('Go Ahead Eagles', 17, 2014)]
    #         for tuple in list:
    #             rankings.append(tuple)
    #     else:

    #         url = ('http://footballdatabase.com/league-scores-tables/netherlands-eredivisie-20'
    #                + str(i) + '-' + str(i + 1))
    #         site = requests.get(url)
    #         content = BeautifulSoup(site.content, 'html.parser')
    #         table = content.findAll('table')[0]

    #         year = int('20' + str(i))

    #         for table_row in table.select('tr'):
    #             cells = table_row.findAll('td')
    #             if len(cells) > 0:
    #                 club_name = cells[1].text.strip()
    #                 ranking = cells[0].text.strip()
    #                 rankings.append((club_name, int(ranking), year))
    
    for i in range(10, 18):

        print('20' + str(i))

        url = 'https://www.transfermarkt.nl/eredivisie/startseite/wettbewerb/NL1/plus/?saison_id=20' + str(i)
        site = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
        soup  = BeautifulSoup(site.content, 'html.parser')
        table = soup.find('table', 'items')
        print(table)
        time.sleep(15)

    # df = pd.DataFrame(data_points, columns=['club_name', 'tr_begin', 'year'])
    # ranking_df = pd.DataFrame(rankings, columns=['club_name', 'ranking', 'year'])
    # df = df.merge(ranking_df, on=['club_name', 'year'], how='left')
    
    # # remove missing datapoints from dataframe
    # df.dropna(how='any', inplace=True)

    # # range of possible ranks
    # binrange = range(0, 19, 3)
    # # ranges of rank_class
    # labrange = range(1, 7) 

    # # reset ranking to integers
    # df.ranking = df.ranking.astype(int)

    # df['ranking_class'] = pd.cut(df['ranking'], bins=binrange, labels=labrange)

    # df.to_csv('eredivisie-ranking.csv')


def main():

    retrieve_data()


if __name__ == "__main__":
    main()