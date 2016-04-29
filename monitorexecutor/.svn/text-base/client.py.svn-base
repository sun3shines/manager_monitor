# -*- coding: utf-8 -*-

import time
from monitorexecutor.globalx import MONITOR_LOOP_INTERVAL

from monitorexecutor.static.host import start
from monitorexecutor.producer.cpu import pStatCpu
from monitorexecutor.consumer.cpu import cStatCpu
from monitorexecutor.producer.mem import pStatMem
from monitorexecutor.consumer.mem import cStatMem
from monitorexecutor.producer.storage import pStatStorage
from monitorexecutor.consumer.storage import cStatStorage
from monitorexecutor.producer.net import pStatNet
from monitorexecutor.consumer.net import cStatNet
from monitorexecutor.producer.disk import pStatDisk
from monitorexecutor.consumer.disk import cStatDisk
from monitorexecutor.producer.service import pStatService
from monitorexecutor.consumer.service import cStatService
from monitorexecutor.process.filter import ProcessFilter
from monitorexecutor.process.service import ServiceFilter

def main():
    hostUuid = start()    
    ProcessFilter().start()
    ServiceFilter().start()
    
    pStatCpu(hostUuid).start()
    cStatCpu().start()
    pStatMem(hostUuid).start()
    cStatMem().start()
    pStatStorage(hostUuid).start()
    cStatStorage().start()
    pStatNet(hostUuid).start()
    cStatNet().start()
    pStatDisk(hostUuid).start()
    cStatDisk().start()
    pStatService(hostUuid).start()
    cStatService().start()
        
    while True:
        time.sleep(MONITOR_LOOP_INTERVAL)
        
if __name__ == '__main__':
    main()
