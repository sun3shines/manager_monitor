# -*- coding: utf-8 -*-

import Queue
from managerlib.advanced.locklist import lockList
from managerlib.advanced.lockdict import lockDict

cpuQueue = Queue.Queue(1000)
memQueue = Queue.Queue(1000)
diskQueue = Queue.Queue(1000)
netQueue = Queue.Queue(1000)
storageQueue = Queue.Queue(1000)
serviceQueue = Queue.Queue(1000)

MONITOR_DISK_PROCESS = lockList()
MONITOR_SERVICE_PROCESS = lockDict()