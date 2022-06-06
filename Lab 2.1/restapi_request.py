#!/usr/local/bin/python3

import ssl, requests
import  urllib3, json, pprint
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

url = 'https://10.31.70.210:55443'
connection_url = '/api/v1/auth/token-services'
login = 'restapi'
password = 'j0sg1280-7@'
payload_url = '/api/v1/interfaces'
#payload_url_stat'/api/v1/interfaces/GigabitEthernet1/statistics

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
ssv1_session = requests.Session()
ssv1_session.mount(url, Ssl1HttpAdapter())

r = ssv1_session.post(url + connection_url, auth=(login, password), verify=False)
if 200 <= r.status_code <= 299:
    print('token OK')
    token=r.json()["token-id"]
else:
    print('NO token')

header = {"content-type": "application/json",
          "X-Auth-Token": token}

#        pprint.pprint(sorted(data['processes'], key=lambda x: x['memory-used'], reverse=True)[:10])

responce = ssv1_session.get(url + payload_url, headers=header, verify=False)
#pprint.pprint(responce.json())
interfaces=responce.json()
#print(type(interfaces))
#if_names=set()
for i in interfaces['items']:
#    if_names.add(i.get('if-name'))
    stat_responce = ssv1_session.get(url + payload_url + '//' + i.get('if-name') + '//statistics', headers=header, verify=False)
    pprint.pprint(stat_responce.json())

#pprint.pprint(sorted(interfaces['items'], key=lambda x: x['if-name']))
#interfaces_list=interfaces_list.append(interfaces['items'], key=lambda x: x['if-name'])

