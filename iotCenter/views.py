from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import urllib.request
import urllib.error
from .models import visitor

def saveLog(request, page):
    pagename = page
    try:
        hit = visitor()
        hit.pagename = pagename
        hit.ip = request.META.get("REMOTE_ADDR", "")
        hit.timestamp = datetime.now()
        hit.referer = request.META.get("HTTP_REFERER", "")
        hit.user_agent = request.META.get("HTTP_USER_AGENT", "")
        hit.save() #save in database
    except:
        pass

# Create your views here.
def test(request):
    return render(request, 'iotCenter/test.html')

def test2(request):
    return render(request, 'iotCenter/test2.html')

def neonlights(request, page):
    saveLog(request, page)
    return render(request, 'iotCenter/neonlights.html')
    #text =
    #content = urllib.request.urlopen("http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/6/0").read()
    #return HttpResponse(content)

def neonShakeOn(request, page):
    saveLog(request, page)
    validStr = "Pin D4 set to 1"
    openUrl = urllib.request.Request('http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/4/1')
    tryCount = 0
    while tryCount < 10:
        try:
            content = urllib.request.urlopen(openUrl).read()
        except urllib.error.URLError as e:
            content = e.reason
        if validStr in str(content):
            break
        tryCount += 1
    if(tryCount >= 10):
        return HttpResponse("timeout")
    else:
        return HttpResponse("success")

def neonShakeOff(request, page):
    saveLog(request, page)
    validStr = "Pin D4 set to 0"
    openUrl = urllib.request.Request('http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/4/0')
    tryCount = 0
    while tryCount < 10:
        try:
            content = urllib.request.urlopen(openUrl).read()
        except urllib.error.URLError as e:
            content = e.reason
        if validStr in str(content):
            break
        tryCount += 1
    if(tryCount >= 10):
        return HttpResponse("timeout")
    else:
        return HttpResponse("success")


def neonSwipeLeftOn(request, page):
    saveLog(request, page)
    validStr = "Pin D5 set to 1"
    openUrl = urllib.request.Request('http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/5/1')
    tryCount = 0
    while tryCount < 10:
        try:
            content = urllib.request.urlopen(openUrl).read()
        except urllib.error.URLError as e:
            content = e.reason
        if validStr in str(content):
            break
        tryCount += 1
    if(tryCount >= 10):
        return HttpResponse("timeout")
    else:
        return HttpResponse("success")

def neonSwipeLeftOff(request, page):
    saveLog(request, page)
    validStr = "Pin D5 set to 0"
    openUrl = urllib.request.Request('http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/5/0')
    tryCount = 0
    while tryCount < 10:
        try:
            content = urllib.request.urlopen(openUrl).read()
        except urllib.error.URLError as e:
            content = e.reason
        if validStr in str(content):
            break
        tryCount += 1
    if(tryCount >= 10):
        return HttpResponse("timeout")
    else:
        return HttpResponse("success")

def neonSwipeRightOn(request, page):
    saveLog(request, page)
    validStr = "Pin D6 set to 1"
    openUrl = urllib.request.Request('http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/6/1')
    tryCount = 0
    while tryCount < 10:
        try:
            content = urllib.request.urlopen(openUrl).read()
        except urllib.error.URLError as e:
            content = e.reason
        if validStr in str(content):
            break
        tryCount += 1
    if(tryCount >= 10):
        return HttpResponse("timeout")
    else:
        return HttpResponse("success")

def neonSwipeRightOff(request, page):
    saveLog(request, page)
    validStr = "Pin D6 set to 0"
    openUrl = urllib.request.Request('http://tunnel40011.remotuino.fullrank.cc:81/arduino/digital/6/0')
    tryCount = 0
    while tryCount < 10:
        try:
            content = urllib.request.urlopen(openUrl).read()
        except urllib.error.URLError as e:
            content = e.reason
        if validStr in str(content):
            break
        tryCount += 1
    if(tryCount >= 10):
        return HttpResponse("timeout")
    else:
        return HttpResponse("success")
