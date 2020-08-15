import mongoengine as me

""" Models """

class Project(me.EmbeddedDocument):
    filename = me.StringField(required=True)
    dofile = me.StringField()

# add more stuff e.g. email, salted password, etc
class User(me.Document):
    username = me.StringField(required=True, primary_key=True)
    projects = me.ListField(me.EmbeddedDocumentField(Project)) # list of embeds




""" Controllers """

def getAllUsers():
    return User.objects()

def getUser(username):
    return User.objects.get(username=username)

def addUser(user):
    newUser = User(username=user['username'])
    return newUser.save(force_insert=True)

""" didn't get this to work """
# def editUser(username, user):
#     User.objects(username=username).update(username=user['username'])
#     return User.objects.get(username=username)

    # userDoc.update(username=user['username'])
    # newUser = User(username=user['username'])
    # return newUser.save()

def deleteUser(username):
    return User.objects.get(username=username).delete()
