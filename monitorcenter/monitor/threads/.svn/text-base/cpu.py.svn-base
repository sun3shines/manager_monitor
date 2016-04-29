# -*- coding: utf-8 -*-

import threading
from monitorcenter.monitor.globalx import GlobalQueue
from managerlib.db.table.static.host import uuid2hostid
from monitorcenter.monitor.mirror.cpu import MirrorCpu
from managerlib.db.table.lock.mysql import getdb

class StatCpu(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.db = getdb()
        self.hostUuid = hostUuid
        
    def run(self):
        q = GlobalQueue.get(self.hostUuid).get('statCpu')
        hostid = uuid2hostid(self.db, self.hostUuid)
        m = MirrorCpu(self.db,hostid)
        while True:
            attr = q.get()
            m.append(attr)
