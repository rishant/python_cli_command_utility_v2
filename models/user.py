from bson import ObjectId


class User:
    def __init__(self, username: str, email: str, password: str, _id: ObjectId = None):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(doc: dict) -> 'User':
        return User(
            username=doc.get('username'),
            email=doc.get('email'),
            password=doc.get('password'),
            _id=doc.get('_id')
        )

    def to_dict(self) -> dict:
        doc = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
        if self.id:
            doc['_id'] = self.id
        return doc
