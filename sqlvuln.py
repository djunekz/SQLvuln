# -*- coding: utf-8 -*-
import os
os.system ("clear")

print ("""\033[31m------------------------------------------\033[0m\n\033[31m ____   ___  _      __     __     _	  \033[0m\n\033[31m/ ___| / _ \| |     \ \   / /   _| |_ __  \033[0m\n\033[31m\___ \| | | | |      \ \ / / | | | | '_ \ \033[0m\n\033[77m ___) | |_| | |___    \ V /| |_| | | | | |\033[0m\n\033[77m|____/ \__\_\_____|    \_/  \__,_|_|_| |_|\033[0m\n	\33[36;1mVersion\33[32;1m 1.0\33[0m\n\n\033[36;1mAuthor\033[0m :\33[33;1m D J U N E K Z\33[0m\n\33[36;1mGithub\33[0m :\33[33;1m https://github.com/djunekz\33[0m\n\33[36;1mCreate Scrypt\33[0m :\n\33[31m     _  _                  _\33[0m\n\33[31m  __| |(_)_   _ _ __   ___| | __ ____\33[0m\n\33[31m / _` || | | | | '_ \ / _ \ |/ /|_  /\33[0m\n\33[55m| (_| || | |_| | | | |  __/   <  / /\33[0m\n\33[55m \__,_|/ |\__,_|_| |_|\___|_|\_\/___|\33[0m\n\33[55m     |__/\33[0m\n\033[31m------------------------------------------\033[0m""")

import sys

if sys.version_info < (3,0):
    sys.exit("Please use python3")

import os, re
import urllib.request
import random
import urllib3
import datetime

class SqlScan:

    __counter = 1
    __maxPage = 2
    __hasil = []
    __vuln = []
    __nothing = []
    __error = []
    
    __mysql_error = [ # do you have another error of sql ? add here ...
        "You have an error in your SQL syntax",
        "MySQL server version for the right syntax to use near",
        "SELECT * FROM"]

    @classmethod
    def dorking(cls,dork=None,max_page=2):
        cls.__maxPage = max_page
        while(cls.__counter < cls.__maxPage):
            try:
                url = "http://www1.search-results.com/web?q="+dork+"&page="+str(cls.__counter)
                req = urllib.request.urlopen(url);
                results = req.read()
                results = results.decode("utf8")
                regx = re.findall(r"<a.class=\"algo-[\D]*\".href=\"(.*?)\"",results)
                for i in regx:
                    cls.__hasil.append(i)
                cls.__counter += 1
            except (Exception, KeyboardInterrupt):
                exit(0)

    # set color
    __danger = "\033[31m"
    __success = "\33[32m"
    __reset = "\033[0m"
    
    @classmethod
    def show(cls,text,exp=None):
        x = None
        if exp in ["err","error","e"]: x = "[ "+cls.__danger+"✕ "+cls.__reset+"] ERROR "+cls.__danger+"=> "+cls.__reset
        else: x = "["+cls.__success+" ✓"+cls.__reset+" ] OK! "+cls.__success+"=> "+cls.__reset
        print(str(x)+" "+text)

    @classmethod
    def scan(cls):
        date = "="*20 + " " + datetime.datetime.now().strftime("%d %h-%m-%Y") # Print this variable to showing date and time now.
        try:
            (dork, max_p) = str(input("\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Enter your Dork \33[32;1m[\33[0mmisal: \33[1;33mproduct.php?id=\33[0m\33[32;1m]\33[0m: ")), int(input("\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Max page \33[32;1m[\33[0minteger\33[32;1m]\33[0m: "))
            cls.dorking(dork,max_p)
            for target in set(cls.__hasil):
                try:
                    req = urllib.request.urlopen(target+"'")
                    html = req.read()
                    html = html.decode("utf8")
                    for sql_error in cls.__mysql_error:
                        if re.search(r""+sql_error.lower(),html.lower()):
                            cls.__vuln.append(target)
                            cls.show(str(target))
                            break
                        else:
                            cls.__nothing.append(target)
                            continue
                except (Exception) as e:
                    cls.__error.append(target)
                    cls.show(str(str(target)+" [ "+cls.__danger+str(e)+cls.__reset)+" ]","e")
                except KeyboardInterrupt:
                    sys.exit("\n")
        except KeyboardInterrupt:
            sys.exit("\n")

        print("\n\n\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Scanning success..\n\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Vuln: \33[32m{}\33[0m\n\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Not vuln: \33[33m{}\33[0m\n\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Error: \33[31m{}\33[0m".format(
            len(set(cls.__vuln)),
            len(set(cls.__nothing)),
            len(set(cls.__error))))

SqlScan().scan()
