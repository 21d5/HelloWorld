"""
@modified from: https://github.com/graphql-python/graphene/blob/master/examples/simple_example.py
"""
import graphene


class Patron(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()


class Query(graphene.ObjectType):

    patron = graphene.Field(Patron)

    def resolve_patron(self, args, context, info):
        """获取 patron 的数据"""
        return Patron(id=1, name='Syrus', age=27)

schema = graphene.Schema(query=Query)
query = '''
    query something{
      patron {
        id
        name
        age
      }
    }
'''

def test_query():
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {
        'patron': {
            'id': '1',
            'name': 'Syrus',
            'age': 27,
        }
    }


if __name__ == '__main__':
    result = schema.execute(query)
    print('query: ', query)
    print('resp: ', result.data)
    # resp:  OrderedDict([('patron', OrderedDict([('id', '1'), ('name', 'Syrus'), ('age', 27)]))])