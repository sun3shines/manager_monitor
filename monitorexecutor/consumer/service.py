# -*- coding: utf-8 -*-

import threading
from monitorexecutor.global_cache import serviceQueue
from monitorexecutor.http.api import monitor_stat

class cStatService(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = serviceQueue
        
    def run(self):
        while True:
            monitor_stat(self.queue.get())
    
    
    