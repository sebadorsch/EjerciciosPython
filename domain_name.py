from urllib.parse import urlparse


def domain_name(url):
    urlparsed = urlparse(url)
    domain = ""
    if urlparsed[1] != "":
        a = urlparsed[1].split('.')
        if urlparsed[1].find('www'):
            domain = a[1]
        else:
            domain = a[0]
    elif urlparsed[1] != "":
        pass
    return domain


if __name__ == '__main__':
    print(domain_name("www.xakep.ru"), "xakep")
    print(domain_name("http://google.com"), "google")
    print(domain_name("http://google.co.jp"), "google")

    print(domain_name("https://youtube.com"), "youtube")
    """
    
    """