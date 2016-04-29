# -*- coding: utf-8 -*-

import threading
from monitorexecutor.global_cache import storageQueue
from monitorexecutor.http.api import monitor_stat

class cStatStorage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = storageQueue
        
    def run(self):
        while True:
            monitor_stat(self.queue.get())
    
    
    