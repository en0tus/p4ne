#!/usr/local/bin/python3

from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, ip_start, ip_end, mask_start, mask_end):
        IPv4Network.__init__(self,
                             (random.randint(ip_start, ip_end),
                              random.randint(mask_start, mask_end)),
                             strict=False
                             )

    def regular(self):
        return self.is_global and not \
            (self.is_multicast or self.is_link_local or \
             self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)

    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

#ip_start=0x0B000000
#ip_end=0xDF000000
#mask_start=0
#mask_end=32

# Служебная функция для передачи в качестве параметра в функцию sorted
def sortfunc(x):
    return x.key_value()

# Инициализируем генератор случайных чисел и список
random.seed()

rnlist = []

# Генерируем сети, помещаем в список
while len(rnlist) < 50:
    random_network = IPv4RandomNetwork(0x0B000000, 0xDF000000, 8, 24)
    if random_network.regular() and random_network not in rnlist: # проверка на регулярность и уникальность
        rnlist.append(random_network)

# И выводим на экран
for n in sorted(rnlist, key=sortfunc):
    print(n)