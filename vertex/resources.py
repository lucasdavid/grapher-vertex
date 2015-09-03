from grapher import resources
from grapher.commons import Cardinality


class Home(resources.Resource):
    description = 'Grapher\'s Home Page'
    methods = ('GET',)

    def get(self):
        return self.response({'hello': 'world'})


class User(resources.EntityResource):
    description = 'Users, such as students, professors and researches.'

    schema = {
        'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 4},
        'email': {'type': 'string', 'required': False, 'empty': False, 'index': True},
        'password': {'type': 'string', 'required': True, 'empty': False, 'minlength': 6, 'visible': False},
    }


class Group(resources.EntityResource):
    schema = {
        'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 2},
    }


class Founder(resources.RelationshipResource):
    origin = Group
    target = User
    cardinality = Cardinality.one

    schema = {
        'at': {'type': 'datetime'}
    }


class Members(resources.RelationshipResource):
    origin = Group
    target = User
    cardinality = Cardinality.many

    schema = {
        'since': {'type': 'string'}
    }
