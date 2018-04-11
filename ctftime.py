#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys, getopt
import requests
import datetime


def print_ctf(ctfs):
    key_list = (
        ('title', 40),
        ('onsite', 10),
        ('start', 12),
        ('finish', 12),
        ('url', 40),
        ('format', 20),
        ('participants', 12),
        ('ctftime_url', 40)
    )
    head = ''
    for (header, format) in key_list:
        f = '| {:' + str(format)[0:format - 2] + 's}'
        head += f.format(str(header)) + ' '
    print head
    for ctf in ctfs:
        line = ''
        for (key, format) in key_list:
            f = '| {:' + str(format) + 's}'
            if not isinstance(ctf[key], str):
                line += f.format(str(ctf[key])[0:format - 2]) + ' '
            else:
                line += f.format(ctf[key].encode('utf-8')[0:format - 2]) + ' '
        print line


def call_api(start, finish, limit=100):
    params = {
        'limit': limit,
        'start': start,
        'finish': finish}
    url = 'https://ctftime.org/api/v1/events/'
    r = requests.get(url, params=params)
    return r.json()


def main(argv):
    now = datetime.datetime.now()
    startd = 0
    endd = 10
    try:
        startd = -int(argv[0])
    except IndexError:
        pass

    try:
        endd = int(argv[1])
    except IndexError:
        pass

    start = now + datetime.timedelta(days=startd)
    end = now + datetime.timedelta(days=endd)
    r = call_api(start.strftime("%s"), end.strftime("%s"))
    print_ctf(r)
    return 'ok'


if __name__ == '__main__':
    if len(sys.argv) > 0:
        main(sys.argv[1:])
    else:
        main([])
