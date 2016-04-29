# -*- coding: utf-8 -*-

from managerapi.missions.tasks.task import Task 

import json
from managerapi.missions.tasks.task import Task
from managerlib.urls.flask import strQuotaGet,strQuotaSet

class QuotaGet(Task):

    def __init__(self,atName):
        self.atName = atName
        
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
    def getUrl(self):

        return strQuotaGet
    
class QuotaSet(Task):

    def __init__(self,atName,val):
        self.atName = atName
        self.val = val
        
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'val':self.val})
    
    def getUrl(self):
        return strQuotaSet
    
