# Library of some of the practical and complex function in Python 3+
# amir.aakhan@gmail.com


def get_url_contents(url):
    import ssl
    import certifi
    from urllib.request import urlopen

    data = urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
    return data.read().decode("utf-8") 


def get_url_contents2(url):
    import os
    return os.popen("curl -s "+url).read()

def get_file_contents(path_file):
    from pathlib import Path
    return Path(path_file).read_text()


def get_string_between(s, start, end):
    return s.split(start)[1].split(end)[0]


def get_array_strings_between(str, start, end):

    strings = []
    for c in str.split(start): 
        spos = c.find(end)
        if spos!=-1:
            strings.append(c[:spos])
    return strings


def remove_html(x):
    import re
    return re.sub('<[^<]+?>', '', x).strip()


def send_mail(to_email, subject, message, from_name, domain, pwd):

    import smtplib
    from email.message import EmailMessage

    server = 'mail.'+domain 
    from_email = 'mailer@'+domain
    
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_name+'<'+from_email+'>'
    msg['To'] = ', '.join(to_email)
    msg.add_header('Content-Type','text/html')
    msg.set_payload(message)

    s = smtplib.SMTP(server, 587)
    # s.set_debuglevel(1)
    s.starttls()
    s.login(from_email, pwd)
    s.send_message(msg)
    s.quit()

    return True


def get_public_ip():

    import os
    ifconfig = str(os.popen("ifconfig").read()).split('\n')
    return get_string_between(ifconfig[1], 'inet ', '  netmask')


def get_public_ip2():
    from requests import get
    json_data = get('http://ip.jsontest.com/').json() # ~ 279 ms
    return json_data['ip']


def download_url_rename(url, old_file, new_file):
    import os
    os.popen("curl -O -s "+url).read()
    os.rename(old_file, new_file)


def copy_file(old_file, new_file):
    import shutil
    shutil.copy(old_file, new_file)


def slugit(x):
    return x.replace(" ", "-").lower()


def get_address_coords(addr, key):
    import requests
    req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+addr+'&key='+key)
    resp = req.json()

    if resp['status'] != 'ZERO_RESULTS':
        lat = resp['results'][0]['geometry']['location']['lat']
        long = resp['results'][0]['geometry']['location']['lng']
        return lat, long
    else:
        return 0, 0


def get_coords_address(lat, long, key):
    from geopy.geocoders import GoogleV3
    geolocator = GoogleV3(api_key=key)
    loc = geolocator.reverse(str(lat)+','+ str(long))
    if loc != None:
        return loc.address
    else:
        return ''
    

def py_mkdir(path):
    import os
    os.makedirs(path, exist_ok=True)


def webp2jpg(webp_file, to_file, to_format):
    # pip3 install Pillow
    from PIL import Image
    im = Image.open(webp_file).convert("RGB")
    if(to_format == 'jpeg'):
        ext = x = to_format.replace('jpeg', 'jpg')
    else:
        ext = to_format
    im.save(to_file+'.'+ext, to_format)


def remove_whitespace(x):
    return ' '.join(x.strip().split())


def get_url_json(url):
    import json
    c = get_url_contents2(url)
    return json.loads(c)


def today_datetime_formatted(f):
    # %d/%m/%Y %H:%M:%S
    from datetime import date
    return date.today().strftime(f)

def read_file(f):
    return open(f, "r").read()


def get_url_emulate(url):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.content

def str_replace(srch, rplc, sbjct):
    if len(sbjct) == 0:
        return ''

    if len(srch) == 1:
        return sbjct.replace(srch[0], rplc[0])

    lst = sbjct.split(srch[0])
    reslst = []
    for s in lst:
        reslst.append(str_replace(s, srch[1:], rplc[1:]))
    return rplc[0].join(reslst);


def django_mysql_format(dt):
    from dateutil.parser import parse
    d = parse(str(dt))
    return d.strftime("%Y-%m-%d")

def get_todate():
    import datetime
    return datetime.datetime.now().date()

def set_session(request, param, value):
    request.session[param] = value

def get_session_param(request, param):
    return request.session.get(param)

def get_session_all(request):
    c = {}
    c['fname'] = request.session.get('fname')
    c['email'] = request.session.get('email')
    c['company_id'] = request.session.get('company_id')
    c['company_name'] = request.session.get('company_name')
    return c

def logout(request):
    for key in request.session.keys():
        request.session[key] = ''
    return redirect('/')

def get_random(x, y):
    import random
    return random.randint(x, y)


def raw_db_sql(sql, keys):
    from django.db import connection, transaction
    cursor = connection.cursor()

    # usage    
    # keys = ('fname', 'email')
    # sql = "SELECT m.fname, m.email FROM team_member m"
    # m = raw_db_sql(sql, keys)
    # c['fname'] = m[0]['fname']

    # eg 2
    # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])

    # eg 3: update etc
    # # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    # # transaction.commit_unless_managed()

    cursor.execute(sql)
    rows = cursor.fetchall()
    return db2json(rows, keys)

def db2json(rows, keys):
    import json
    result = []
    for row in rows:
        result.append(dict(zip(keys,row)))
    json_data = json.dumps(result)
    return  json.loads(json_data)


def list_str_diff(list1, list2):
    res = [ ele for ele in list1 ]
    for a in list2:
        if a in list1:
            res.remove(a)
    return res
