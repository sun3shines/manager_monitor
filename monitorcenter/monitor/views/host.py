# -*- coding: utf-8 -*-

import json
import Queue

from managerlib.common.bufferedhttp import jresponse
from managerlib.db.table.static.host import puth,uuid2hostid
from managerlib.db.table.static.host_cpu import putc
from managerlib.db.table.static.host_mem import putms
from managerlib.db.table.static.host_net import putns
from managerlib.db.table.static.host_disk import putds

from monitorcenter.monitor.globalx import GlobalDb,GlobalQueue,GlobalThread,GlobalClass
from managerlib.db.table.lock.mysql import getdb,getlock
from monitorcenter.monitor.threads.cpu import StatCpu
from monitorcenter.monitor.threads.mem import StatMem
from monitorcenter.monitor.threads.net import StatNet
from monitorcenter.monitor.threads.disk import StatDisk
from monitorcenter.monitor.threads.storage import StatStorage
from monitorcenter.monitor.threads.service import StatService

def processStartUp(request):

    param = json.loads(request.body)
    
    hostUuid = param.get('hostUuid')
    if not GlobalDb.get(hostUuid):
        GlobalDb.put(hostUuid, getdb())
        
    db = GlobalDb.get(hostUuid)
    
    with getlock(db) as mylock:
        puth(db,hostUuid,param.get('hostClass'))
        hostid = uuid2hostid(db, hostUuid)
        putc(db, hostid, param.get('cpuClass'))
        putms(db, hostid, param.get('memClass'))
        putns(db, hostid, param.get('netClass'))
        putds(db, hostid, param.get('diskClass'))
    
    if not GlobalQueue.get(hostUuid):
        loadQueue(hostUuid, GlobalQueue)
        
    if not GlobalThread.get(hostUuid):
        loadThread(hostUuid, GlobalThread)
    
    return jresponse('0','ready',request,200)

def loadQueue(hostUuid,queueDict):
    
    queueDict.put(hostUuid,{})
    for cls in GlobalClass:
        queueDict.get(hostUuid).update({cls:Queue.Queue()})
        
def loadThread(hostUuid,threadDict):
    
    StatCpu(hostUuid).start()
    StatMem(hostUuid).start()
    StatDisk(hostUuid).start()
    StatNet(hostUuid).start()
    StatStorage(hostUuid).start()
    StatService(hostUuid).start()
    
