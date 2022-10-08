
from app.config.bcrypt import get_bcrypt
from app.db.userRepo import addUserRepo
# from passlib.hash import sha256_crypt
# from werkzeug.security import generate_password_hash

def addUserService(first_name,last_name,email,password):

    bcrypt = get_bcrypt()

    # print(""bcrypt)
    pw_hash = bcrypt.generate_password_hash(password)



    # hash_pw = generate_password_hash(password)
    print("Hashed",pw_hash)


    user_details = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": pw_hash

    }

    addUserRepo(user_details)



