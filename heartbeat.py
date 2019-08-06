#!/usr/bin/env python

import requests
import logging

logging.basicConfig(filename='heartbeat.log', filemode='a', format='%(asctime)s - %(message)s')

def heartbeat(server):
    ping = requests.get(server, timeout=5)
    if ping.status_code == 200:
        logging.error('INFO: Server is up and running')
    else:
        logging.error('ERROR: Failed to reach server')
