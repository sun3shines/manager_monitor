
from managerlib.restful.cloudfs.http.mission import Mission
from managerlib.restful.cloudfs.http.advanced_task import UserInit

def libUserRegister(atName,token):
    ev = Mission(atName,token)
    t = UserInit()
    ev.http(t)
    return t.response
    