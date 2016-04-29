# -*- coding: utf-8 -*-
from managerlib.db.table.user import userDisable,userEnable
from managerlib.db.db_user import user_list

# urDelete -> db_flask_user_delete
# urEnable -> db_flask_user_enable
# urDisable -> db_flask_user_disable
# urList -> db_flask_user_list

def db_flask_user_delete(db,userName):
    return userDisable(db, userName)

def db_flask_user_enable(db,userName):
    return userEnable(db, userName)

def db_flask_user_disable(db,userName):
    return userDisable(db, userName)

def db_flask_user_list(db):
    return user_list(db)