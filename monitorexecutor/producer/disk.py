# -*- coding: utf-8 -*-

import threading
from monitorexecutor.global_cache import diskQueue
from monitorexecutor.dynamic.stat_disk import get_psutil_disk

class pStatDisk(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.queue = diskQueue
        self.hostUuid = hostUuid
        
    def run(self):
        for data in get_psutil_disk(self.hostUuid):
            print data
            self.queue.put(data,block=True)
    
