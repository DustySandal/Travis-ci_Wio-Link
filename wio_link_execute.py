#!/usr/bin/env python
# copyright 2015 seeed, wangtengoo7@gmail.com
import sys
import requests
import threading

red_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayD0/onoff/1?access_token=5705ddcf8ef1600ed5016f66c8d535c6"
red_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayD0/onoff/0?access_token=5705ddcf8ef1600ed5016f66c8d535c6"
orange_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayD1/onoff/1?access_token=5705ddcf8ef1600ed5016f66c8d535c6"
orange_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayD1/onoff/0?access_token=5705ddcf8ef1600ed5016f66c8d535c6"
green_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayD2/onoff/1?access_token=5705ddcf8ef1600ed5016f66c8d535c6"
green_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayD2/onoff/0?access_token=5705ddcf8ef1600ed5016f66c8d535c6"

def post_url(url):
    r = requests.post(url)
    print r.status_code
    if r.status_code != 200:
        requests.post(url)


def main(argv):
    status = argv
    if status == "success":
        urls =[red_led_off_api, orange_led_off_api, green_led_on_api]
    elif status == "failure":
        urls =[red_led_on_api, orange_led_off_api, green_led_off_api]
    elif status == "building":
        urls =[red_led_off_api, orange_led_on_api, green_led_off_api]

    for url in urls:
        threading.Thread(target=post_url, args=(url,)).start()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python wio_link_execute [success/failure/building]'
        exit(1)
    main(sys.argv[1])
