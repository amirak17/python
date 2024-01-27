
def get_string_between(s, start, end):
    return s.split(start)[1].split(end)[0]


def file_get_contents(url):
    import ssl
    import certifi
    from urllib.request import urlopen

    data = urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
    return data.read().decode("utf-8") 


def get_array_strings_between(str, start, end):

    strings = []
    for c in str.split(start): 
        spos = c.find(end)
        if spos!=-1:
            strings.append(c[:spos])
    return strings


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

    server = smtplib.SMTP(server, 587)
    # server.set_debuglevel(1)
    server.starttls()
    server.login(from_email, pwd)
    server.send_message(msg)
    server.quit()

    return True


def get_public_ip():

    import os
    ifconfig = str(os.popen("ifconfig").read()).split('\n')
    return get_string_between(ifconfig[1], 'inet ', '  netmask')


def get_public_ip2():
    from requests import get
    json_data = get('http://ip.jsontest.com/').json() # ~ 279 ms
    return json_data['ip']

