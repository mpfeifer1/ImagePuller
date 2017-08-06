import sys, os, requests, shutil

def main():
    url1 = 'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid='
    url2 = '&type=card'

    basepath = os.path.dirname(os.path.abspath(__file__))+'/cards/'
    for i in sys.stdin:
        i = i.split()[1]
        i = str(int(str(i)))

        r = requests.get(url1 + i + url2, stream=True)
        if r.status_code == 200:
            print i
            path = basepath + i + '.png'
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            print i + " FAILED"

if __name__ == "__main__":
    main()
