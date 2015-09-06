from grapher import commons, errors
from grapher.repositories.base import EntityRepository


class CachedRepository(EntityRepository):
    data = {}

    def where(self, skip=0, limit=None, **query):
        query_item = query.popitem()
        if query_item[0] == self.identity:
            return self.find((query_item[1]))

        return []

    def create(self, entities):
        result = []

        for entity in entities:
            self.data[entity[self.identity]] = entity
            del entity[self.identity]

            result.append(entity)

        return result

    def all(self, skip=0, limit=None):
        return commons.CollectionHelper.restore_enumeration(self.data, False)

    def delete(self, identities):
        result = []

        for identity in identities:
            result.append(self.data[identity])
            del self.data[identity]

        return result

    def find(self, identities):
        try:
            return [self.data[i] for i in identities]

        except KeyError:
            raise errors.NotFoundError(('NOT_FOUND', identities))

    def update(self, entities):
        result = []

        for entity in entities:
            identity = entity[self.identity]
            del entity[self.identity]

            self.data[identity].update(entity)
            result.append(self.data[identity])

        return result
