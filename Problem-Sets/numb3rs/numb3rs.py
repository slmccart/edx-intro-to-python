import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #return bool(re.match(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip))
    # 3 parts for number matching
    #.  1) 0-199
    #.  2) 200-249
    #.  3) 250-255
    return bool(re.match(r"^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip))


if __name__ == "__main__":
    main()
