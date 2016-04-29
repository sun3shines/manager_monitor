
from managerlib.restful.cloudfs.http.advanced_task import FileMeta
from managerlib.restful.cloudfs.http.basic_task import UfoContainerMeta,UfoContainerList
from managerlib.restful.cloudfs.http.mission import Mission

def libGetContainerList(atName,token):
    
    ev = Mission(atName,token)
    t = UfoContainerList()
    t = ev.http(t)
    return t.response

def libGetContainerMeta(atName,token,path):
    
    ev = Mission(atName,token)
    t = UfoContainerMeta(path)
    t = ev.http(t)
    return t.response

