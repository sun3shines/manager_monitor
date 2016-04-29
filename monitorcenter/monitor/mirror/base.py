# -*- coding: utf-8 -*-

from monitorcenter.monitor.globalx import MIRROR_LIMIT

class MirrorBase(object):
    def __init__(self,db,hid):
        self.db = db
        self.hid = hid
        self.currentindex = 0
        self.currentseq = 0
        self.l = []
        self.c = self.getClass()
        self.load()
            
    def load(self):
        self.l = self.hid2attrs(self.db, self.hid)
        if MIRROR_LIMIT == len(self.l):
            
            maxseq = -1 
            for attr in self.l:
                seq = float(attr[self.c.seq]) 
                if seq > maxseq:
                    maxseq = seq
                    self.currentindex = self.currentindex + 1
            self.currentseq = maxseq + 1
            
        else:
            self.currentindex = len(self.l)

            maxseq = -1
            for attr in self.l:
                seq = float(attr[self.c.seq])
                if seq > maxseq:
                    maxseq = seq
            self.currentseq = maxseq + 1

            while len(self.l) < MIRROR_LIMIT:
                self.l.append(self.emptyObject)
            
    def append(self,attr):

        if MIRROR_LIMIT == self.currentindex:
            self.currentindex = 0
            self.l = self.hid2attrs(self.db, self.hid)
        self.update(attr)
        self.currentindex = self.currentindex + 1
        self.currentseq = self.currentseq + 1
    
    def update(self,attr):
        mirror_attr = self.l[self.currentindex]
    
        # 之前是因为误判了。是0 而不是None 
        if None == mirror_attr.get(self.c.seq):
            self.insert_db(attr)
        else:
            self.update_db(attr,mirror_attr)
        self.update_mirror(attr,mirror_attr)

    @property
    def hid2attrs(self):
        pass
    
    @property
    def getClass(self):
        pass
    
    @property
    def emptyObject(self):
        pass
            
    def insert_db(self,attr):
        pass
        
    def update_db(self,attr,mirror_attr):
        pass
    
    def update_mirror(self,attr,mirror_attr):
        pass
