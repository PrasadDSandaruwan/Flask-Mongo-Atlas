from app.config.db import get_db
from werkzeug.local import LocalProxy



db = LocalProxy(get_db)


def addUserRepo(userDetails):
    db.user.insert_one(userDetails)

