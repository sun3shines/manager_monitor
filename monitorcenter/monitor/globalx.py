# -*- coding: utf-8 -*-

from managerlib.advanced.lockdict import lockDict

GlobalDb = lockDict()

GlobalThread = lockDict()

GlobalQueue = lockDict()

GlobalClass = ['host','statCpu','statMem','statNet','statDisk','statStorage',
               'statService']

MIRROR_LIMIT = 100
