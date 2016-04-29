# -*- coding: utf-8 -*-

from managerlib.common.exceptions import LockTimeout, MessageTimeout
from managerlib.common.bufferedhttp import jresponse
from managerlib.urls.monitor import *

from monitorcenter.monitor.views.host import processStartUp
from monitorcenter.monitor.views.stat import processStatData

url2view = {}

url2view.update({urlStartUp:processStartUp})

url2view.update({urlStatData:processStatData})

def handlerequest(req):

    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req)
