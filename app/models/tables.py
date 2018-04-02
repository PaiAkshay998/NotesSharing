from app import db

class User(db.Model):
    username = db.Column(db.String(60), primary_key=True)
    year = db.Column(db.Integer)
    dept = db.Column(db.String(60))
    authenticated= db.Column(db.Boolean,default=False)
    #nickname = db.Column(db.String(64), index=True)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def __repr__(self):
        return '<User %r>' % (self.username)


class Department(db.Model):
    department = db.Column(db.String(64), primary_key=True)

    def is_authenticated(self):
        # Return False if the user object is not allowed for some reason
        return True

    def is_active(self):
        return True  # Return False if they are banned

    def __repr__(self):
        return '<Department %r>' % (self.department)


class files(db.Model):
    __searchable__ = ['department','description','author','tags'] #array with all the database fields that will be in the searchable index
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), index=True)
    department = db.Column(db.String(64), index=True)
    semester = db.Column(db.Integer, index=True)
    author = db.Column(db.String(64), index=True)
    description = db.Column(db.String(100), index=True)
    downloads = db.Column(db.Integer, index=True)
    uploader = db.Column(db.String(64), index=True)
    upload_date = db.Column(db.DateTime(), index=True)
    def __repr__(self):
        return '<File {0}-> {1} >'.format(self.filename, self.department)

class Tags(db.Model):
    # this table will be in the form (file_id, tag)
    id = db.Column(db.Integer, primary_key=True)
    fileid = db.Column(db.Integer, db.ForeignKey('files.id'), index=True)
    tag = db.Column(db.String(64), index=True)

class TagDetails(db.Model):
    # this table will contain data describing each tag
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64), primary_key=True, index=True)
    description = db.Column(db.String(100), index=True)

class stars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer)
    starrer = db.Column(db.String(64), index=True)
