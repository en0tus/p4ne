import requests, json, pprint, ssl

#from flask import Flask, render_template, jsonify
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

url = 'https://10.31.70.210:55443'
login = 'restapi'
password = 'j0sg1280-7@'
connection_url = '/api/v1/auth/token-services'
payload_url = {'/api/v1/global/memory/processes','/api/v1/interfaces'}

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
ssv1_session = requests.Session()
ssv1_session.mount(url, Ssl1HttpAdapter())

def get_token():
    r = ssv1_session.post(url + connection_url, auth=(login, password), verify=False)
    if 200 <= r.status_code <= 299:
#        print('token OK')
        return r.json()["token-id"]
    else:
#        print('NO token')
        return None

new_token = get_token()
header = {
    "content-type": "application/json",
    "X-Auth-Token": new_token
}

for i in payload_url:
    responce = ssv1_session.get(url + i, headers=header, verify=False)
    data = responce.json()
    if "processes" in i:
        print('---PROCESSES---')
        pprint.pprint(sorted(data['processes'], key=lambda x: x['memory-used'], reverse=True)[:10])
#        dictionary = sorted(responce.json()['processes'], key=lambda x: x["memory-used"], reverse=True)[0:10]
#        print(dictionary)
    if "interfaces" in i:
        print('---INTERFACES---')
        pprint.pprint(data)