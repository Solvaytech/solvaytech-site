from ..models import StajUser
from django.utils import timezone
from ..generator import KeyGenerator

class Query:

    global register_db
    register_db = "stajDB"

    # USER INFORMATION CHECK

    def checkUserInformationName(user_name):
        if StajUser.objects.using(register_db).filter(name = user_name):
            return False
        return True

    def checkUserInformationEmail(e_mail):
        if StajUser.objects.using(register_db).filter(email = e_mail):
            return False
        return True

    def checkUserExists(**kwargs):
        try:
            for key,value in kwargs.items():
                match key:
                    case "name":
                        if not Query.checkUserInformationName(value):
                            raise Exception("UsernameExists: Given username already exists.")
                    case "email":
                        if not Query.checkUserInformationEmail(value):
                            raise Exception("EmailExists: Given email already exists.")
        except Exception as e:
            return e
        return True

    # ! USER INFORMATION CHECK
    # GET USER DATA

    def getUserInformationPW(user_name, pass_word):
        try:
            val = StajUser.objects.using(register_db).filter(name = user_name, password= pass_word)
            if val:
                return val
            else:
                return False
        except Exception as e:
            return e

    def getUserInformationPasswordRegen(user_name, e_mail, regen_token):
        try:
            val = StajUser.objects.using(register_db).filter(name = user_name, email = e_mail, password_regen = regen_token)
            if val:
                return val
            else:
                return False
        except Exception as e:
            return e

    def getUserInformationEmail(user_name, e_mail):
        try:
            val = StajUser.objects.using(register_db).filter(name = user_name, email = e_mail)
            if val:
                return val
            else:
                return False
        except Exception as e:
            return e

    # ! GET USER DATA
    # CREATING USER

    def createUser(user_name, pass_word, e_mail):
        check = Query.checkUserExists(name = user_name, email = e_mail)
        if isinstance(check, Exception):
            return check
        try:
            user = StajUser(name = user_name,
                            email = e_mail,
                            password = pass_word,
                            create_date = timezone.now())
            user.save(using=register_db)
            return True
        except Exception as e:
            return e

    # ! CREATING USER
    # FORGOT PASSWORD

    def userPasswordRegenStart(user_name, e_mail):
        queryObject = Query.getUserInformationEmail(user_name, e_mail)
        try:
            if isinstance(queryObject, Exception):
                # return queryObject
                raise Exception("LoginError", "Cannot found user for the given information.")
            if not queryObject:
                raise Exception("LoginError", "Cannot found user for the given information.")
        except Exception as e:
            print(e)
            return e
        regen_token = KeyGenerator(length=20).randomGenerateKey()
        queryObject.password_regen = regen_token
        return regen_token

    def userPasswordRegenSet(user_name, e_mail, regen_token):
        queryObject = Query.getUserInformationPasswordRegen(user_name, e_mail, regen_token)
        if isinstance(queryObject, Exception):
            return queryObject

    # ! FORGOT PASSWORD