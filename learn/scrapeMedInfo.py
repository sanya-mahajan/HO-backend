from bs4 import BeautifulSoup
#import requests library
import requests

def get_med_info(text):
    scraped_data = {}
    search_result=" "
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} 
    url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+text+'&btnG=' 
    response=requests.get(url,headers=headers) 
    soup=BeautifulSoup(response.content,'lxml') 
    print(soup.select('[data-lid]')) 
    for item in soup.select('[data-lid]'): 
        try: 
            print('----------------------------------------') 
            #print(item) 
            print(item.select('h3')[0].get_text()) 
            search_result=search_result+str(item.select('h3')[0].get_text())
            #append new line
            search_result=search_result+"\n"
        except Exception as e: 
            raise e 
        print('')
    scraped_data['search_result']=search_result

    
    return scraped_data

