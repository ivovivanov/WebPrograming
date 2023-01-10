import requests
from monitoring import website

def check_websites(websites):
    for url in websites:
        site_status = website.is_alive(url)
        print(f'{url} -> {"OK" if site_status else "Not OK"}')



if __name__ == '__main__':
    monitored_sites = ['google.com', 'alabalanica.bg', 'yahoo.com', 'gmail.com' ]
    check_websites(monitored_sites)


    '''
    google.com -> OK
    msn.com -> OK
    amazon.com -> OK
    asdf.bg -> Not OK
    '''