from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import socket
import smtplib
import dns.resolver
import re


def verify_email(request):
    if request.method == 'GET':
        addressToVerify = request.GET.get('email')
        print(addressToVerify)
        # addressToVerify = 'onkar.sarkate@viit.ac.in'
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        if match == None:
            print('Bad Syntax')
            # raise ValueError('Bad Syntax')
            return HttpResponse('Bad Syntax')
        records = dns.resolver.query('emailhippo.com', 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        # Get local server hostname
        host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host)
        server.mail('official@gsered.com')
        code, message = server.rcpt(str(addressToVerify))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            print('Success')
            return HttpResponse('Success')

        else:
            print('Bad')

            return HttpResponse('Bad')
