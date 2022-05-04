#!/usr/bin/python3
import pprint as pp
import subprocess


def log_dive(apc_log: str, con_ip: str):
    with open(apc_log, "r") as f:
        el = f.readlines()
        el = [line.rstrip() for line in el]
    ip_ct = {}
    for ip in el:
        a = lambda x: ip.split()[0]
        ip_ct[a(ip)] = ip_ct.get(a(ip), 0) + 1
    del ip_ct[con_ip]
    pp.pprint(ip_ct)
    print(f"\nTotal Visits: {sum(ip_ct.values())}\nTotal Unique Visitors: {len(ip_ct)}\nMost Visits From: \
     {max(ip_ct, key=ip_ct.get)}")


def current_ip():
    list2 = []
    c_ip = subprocess.check_output(["who"])
    c_ip = c_ip.decode("utf-8")
    c_ip = c_ip.split()
    for i in c_ip:
        list2.append(i.split(" "))
    cip = list2[-1][-1]
    r_ellipsis = ['(', ')']
    for letter in cip:
        if letter in r_ellipsis:
            cip = cip.replace(letter, "")
    return cip


if __name__ == "__main__":
    apache_log = "/var/log/apache2/access.log"

    log_dive(apache_log, current_ip())