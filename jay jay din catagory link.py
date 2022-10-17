import bs4
import requests
import csv

def function1():

    base_url = "https://www.jaijaidinbd.com/all-news"
    catagory = "information-technology"
    #next_page = "18"

    national_catagory = [""]

    all_url = []
    i=0
    for page_index in national_catagory:
        i=i+1
        if i==1:
            complete_url =  base_url + '/' + catagory + '/'#+ next_page + '/'
            #print(complete_url + '18')
            #print(complete_url + '36')
        else:
            complete_url = base_url + '/' + catagory + '/' +str(page_index)
            #print(complete_url + '18')
            #print(complete_url + '36')
        all_url.append([complete_url])
        all_url.append([complete_url + '?pg=2'])
        all_url.append([complete_url + '?pg=3'])
        all_url.append([complete_url + '?pg=4'])
        all_url.append([complete_url + '?pg=5'])
        all_url.append([complete_url + '?pg=6'])
        all_url.append([complete_url + '?pg=7'])
        all_url.append([complete_url + '?pg=8'])
        all_url.append([complete_url + '?pg=9'])
        all_url.append([complete_url + '?pg=10'])
        all_url.append([complete_url + '?pg=11'])
        all_url.append([complete_url + '?pg=12'])
        all_url.append([complete_url + '?pg=13'])
        all_url.append([complete_url + '?pg=14'])
        all_url.append([complete_url + '?pg=15'])
        all_url.append([complete_url + '?pg=16'])
        all_url.append([complete_url + '?pg=17'])
        all_url.append([complete_url + '?pg=18'])
        all_url.append([complete_url + '?pg=19'])
        all_url.append([complete_url + '?pg=20'])
        all_url.append([complete_url + '?pg=21'])
        all_url.append([complete_url + '?pg=22'])
        all_url.append([complete_url + '?pg=23'])
        all_url.append([complete_url + '?pg=24'])
        all_url.append([complete_url + '?pg=25'])
        all_url.append([complete_url + '?pg=26'])
        all_url.append([complete_url + '?pg=27'])
        all_url.append([complete_url + '?pg=28'])
        all_url.append([complete_url + '?pg=29'])
        all_url.append([complete_url + '?pg=30'])
        all_url.append([complete_url + '?pg=31'])
        all_url.append([complete_url + '?pg=32'])
        all_url.append([complete_url + '?pg=33'])
        all_url.append([complete_url + '?pg=34'])
        all_url.append([complete_url + '?pg=35'])
        all_url.append([complete_url + '?pg=36'])
        all_url.append([complete_url + '?pg=37'])
        all_url.append([complete_url + '?pg=38'])
        all_url.append([complete_url + '?pg=39'])
        all_url.append([complete_url + '?pg=40'])
        all_url.append([complete_url + '?pg=41'])
        all_url.append([complete_url + '?pg=42'])
        all_url.append([complete_url + '?pg=43'])
        all_url.append([complete_url + '?pg=44'])
        all_url.append([complete_url + '?pg=45'])
        all_url.append([complete_url + '?pg=46'])
        all_url.append([complete_url + '?pg=47'])
        all_url.append([complete_url + '?pg=48'])
        # all_url.append([complete_url + '?pg=49'])
        # all_url.append([complete_url + '?pg=50'])
        # all_url.append([complete_url + '?pg=51'])
        # all_url.append([complete_url + '?pg=52'])
        # all_url.append([complete_url + '?pg=53'])
        # all_url.append([complete_url + '?pg=54'])
        # all_url.append([complete_url + '?pg=55'])
        # all_url.append([complete_url + '?pg=56'])
        # all_url.append([complete_url + '?pg=57'])
        # all_url.append([complete_url + '?pg=58'])
        # all_url.append([complete_url + '?pg=59'])
        # all_url.append([complete_url + '?pg=60'])
        # all_url.append([complete_url + '?pg=61'])
        # all_url.append([complete_url + '?pg=62'])
        # all_url.append([complete_url + '?pg=63'])
        # all_url.append([complete_url + '?pg=64'])
        # all_url.append([complete_url + '?pg=65'])
        # all_url.append([complete_url + '?pg=66'])
        # all_url.append([complete_url + '?pg=67'])
        # all_url.append([complete_url + '?pg=68'])
        # all_url.append([complete_url + '?pg=69'])
        # all_url.append([complete_url + '?pg=70'])
        # all_url.append([complete_url + '?pg=71'])
        # all_url.append([complete_url + '?pg=72'])
        # all_url.append([complete_url + '?pg=73'])
        # all_url.append([complete_url + '?pg=74'])
        # all_url.append([complete_url + '?pg=75'])
        # all_url.append([complete_url + '?pg=76'])
        # all_url.append([complete_url + '?pg=77'])
        # all_url.append([complete_url + '?pg=78'])
        # all_url.append([complete_url + '?pg=79'])
        # all_url.append([complete_url + '?pg=80'])
        # all_url.append([complete_url + '?pg=81'])
        # all_url.append([complete_url + '?pg=82'])
        # all_url.append([complete_url + '?pg=83'])
        # all_url.append([complete_url + '?pg=84'])
        # all_url.append([complete_url + '?pg=85'])
        # all_url.append([complete_url + '?pg=86'])
        # all_url.append([complete_url + '?pg=87'])
        # all_url.append([complete_url + '?pg=88'])
        # all_url.append([complete_url + '?pg=89'])
        # all_url.append([complete_url + '?pg=90'])
        # all_url.append([complete_url + '?pg=91'])
        # all_url.append([complete_url + '?pg=92'])
        # all_url.append([complete_url + '?pg=93'])
        # all_url.append([complete_url + '?pg=94'])
        # all_url.append([complete_url + '?pg=95'])
        # all_url.append([complete_url + '?pg=96'])








    with open('main_page_url.csv',mode = 'w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list,delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()
    return all_url
function1()
