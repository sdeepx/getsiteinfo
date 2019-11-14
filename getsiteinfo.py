from requests import *
from socket import *
from sys import exit


def get_ip(url, host, port=80):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))
    print("Ip -> %s : {}".format(host) % url)


def get_info(host):
    if "https://" in host:
        info = get(host).headers
        for i, j in info.items():
            print(i, ": ", j)
    else:
        url = "https://"+host
        info = get(url).headers
        for i, j in info.items():
            print(i, ": ", j)


def main():
    try:
        url = input(" : ")
        if len(url) == 0:
            print("You didn't enter any host name. Enter a url ->")
            return main()

        try:
            ip_url = url
            if "https://" in ip_url:
                filter_host = ip_url.strip("https://")
                host = gethostbyname(filter_host)
            elif "http://" in ip_url:
                filter_host = ip_url.strip("http://")
                host = gethostbyname(filter_host)
            else:
                host = gethostbyname(url)
            get_ip(url, host)
            get_info(url)
        except (gaierror, RequestException, UnicodeError):
            print("Please Check the url. Unable to find data of: ", url)
    except KeyboardInterrupt as ke:
        if ke:
            print("You stop the program.")
            exit()


if __name__ == '__main__':
    main()
