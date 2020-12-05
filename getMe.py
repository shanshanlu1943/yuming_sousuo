import requests
from bs4 import BeautifulSoup

def filer(str):
    arr={'0','1','2','3','4','5','6','7','8','9','10','-'}
    for a in arr:
        if a in str:
            return False
            break
    else:
        return True

def sent_mess(url):
    global myfile
    r = requests.get('https://domain.me/domainsuggest.php?domain={}'.format(url), headers={'User-Agent':'Mozilla/5.0','connection':'close'})
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    for ym in soup.find_all('a'):
        ym = ym.get('href')[40:] + '\n'
        if filer(ym):
            myfile.write(ym)
    print('OverOne')

myfile = open('yuming.txt','w')

def main():
    arr={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','u','r','s','t','u','v','w','x','y','z'}
    for a in arr:
        for b in arr:
            url = a+b
            sent_mess(url)
    global myfile
    myfile.close()

if __name__ == '__main__':
    main()
