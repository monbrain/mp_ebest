## https://docs.graphene-python.org/en/latest/quickstart/

## pip install "graphene>=2.0"

# from graphene import ObjectType, String, Schema

# class Query(ObjectType):
#     # this defines a Field `hello` in our Schema with a single Argument `name`
#     hello = String(name=String(default_value="stranger"))
#     goodbye = String()

#     # our Resolver method takes the GraphQL context (root, info) as well as
#     # Argument (name) for the Field and returns data for the query Response
#     def resolve_hello(root, info, name):
#         return f'Hello {name}!'

#     def resolve_goodbye(root, info):
#         return 'See ya!'

# schema = Schema(query=Query)

# # type Query {
# #   hello(name: String = "stranger"): String
# #   goodbye: String
# # }

# # we can query for our field (with the default argument)
# query_string = '{ hello }'
# result = schema.execute(query_string)
# print(result.data)
# print(result.data['hello'])
# # "Hello stranger!"

# # or passing the argument in the query
# query_with_argument = '{ hello(name: "GraphQL") }'
# result = schema.execute(query_with_argument)
# print(result.data['hello'])
# # "Hello GraphQL!"



# ## https://stackoverflow.com/questions/51837996/how-to-return-json-in-python-graphene-resolver-without-backslashes-before-quotat

# import graphene
# # Our new model
# class Section(graphene.ObjectType):
#     key = graphene.String()        # dictionary key
#     header = graphene.String()     # dictionary value
#     # content = graphene.String()     # dictionary value

# # Your previous schema with modifications
# class Query(graphene.ObjectType):
#     # questionnaire = graphene.types.json.JSONString(description='JSON result test')

#     # Return a list of section objects
#     questionnaire = graphene.List(Section)

#     # def resolve_questionnaire(self, info: graphql.ResolveInfo):
#     def resolve_questionnaire(self, info):
#         sections = {
#           's1': "Section 1",
#           's2': "Section 2",
#           's3': "Section 3",
#           's4': "Section 4"
#         }

#         sections_as_obj_list = [] # Used to return a list of Section types

#         # Create a new Section object for each item and append it to list
#         for key, value in sections.items(): # Use sections.iteritems() in Python2
#             section = Section(key, value) # Creates a section object where key=key and header=value
#             sections_as_obj_list.append(section)

#         # return sections
#         return sections_as_obj_list


# # query {
# #   questionnaire {
# #     key
# #     header
# #   }
# # }

# query_string = """{
#   questionnaire {
#     key
#     header
#   }
# }
# """
# schema = graphene.Schema(query=Query)

# # query_string = '{ hello }'
# result = schema.execute(query_string)
# print(result.data)
# # print(result.data['hello'])
# # # "Hello stranger!"


##@@ https://soyoung-new-challenge.tistory.com/82

import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='Alice', last_login=datetime.now()),
            User(username='Bob', last_login=datetime.now()),
            User(username='Steven', last_login=datetime.now())
        ][:first]

##@@ Query
# schema = graphene.Schema(query=Query)

# result = schema.execute(
#     '''
#     {
#         users(first: 2) {
#             username
#             lastLogin
#         }
#     }
#     '''
# )

# items = dict(result.data.items())
# print(json.dumps(items, indent=4))


##@@ Mutation
class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)


result = schema.execute(
    '''
    mutation createUser($username: String) {
        createUser(username: $username){
            user {
                username
            }
        }
    }
    ''',
    variable_values={'username':'Bob'},
    context={'is_vip': True}
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))