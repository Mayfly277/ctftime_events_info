#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import requests
import datetime
try:
    from prettytable import PrettyTable
except ImportError:
    print('Please install prettytable')
    sys.exit(1)

def print_ctf(ctfs):
    t = PrettyTable()
    t.field_names = ['title', 'onsite', 'start', 'finish', 'url', 'format', 'participants', 'ctftime_url'] # 'description'
    t.align['title'] = 'l'
    t.align['url'] = 'l'
    # t.align['description'] = 'l'
    for ctf in ctfs:
        row = []
        for key in t.field_names:
            if key == 'start' or key == 'finish':
                row.append(ctf[key][0:10])
            else:
                row.append(ctf[key])
        t.add_row(row)
    print(t)


def call_api(start, finish, limit=100):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    params = {
        'limit': limit,
        'start': start,
        'finish': finish}
    url = 'https://ctftime.org/api/v1/events/'
    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()
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
    start_ts = int(start.timestamp())
    end_ts = int(end.timestamp())
    r = call_api(start_ts, end_ts)
    print_ctf(r)
    return 'ok'

if __name__ == '__main__':
    if len(sys.argv) > 0:
        main(sys.argv[1:])
    else:
        main([])
