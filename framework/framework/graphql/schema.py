import strawberry
from strawberry.extensions import QueryDepthLimiter, ValidationCache, ParserCache, AddValidationRules
from strawberry.tools import merge_types
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware

from flights.graphql.mutations import FlightMutations
from flights.graphql.queries import FlightQueries
from user.graphql.mutation.bookings import BookingMutations
from user.graphql.query.booking import BookingQueries
from gqlauth.user.queries import UserQueries
from user.auth.schema import UserMutations


Mutations = merge_types('Mutations', (FlightMutations, UserMutations, BookingMutations))
Query = merge_types('Queries', (FlightQueries, UserQueries, BookingQueries))

extensions = [
    QueryDepthLimiter(max_depth=10),
    ParserCache(maxsize=100),
    ValidationCache(maxsize=100),
    JSONWebTokenMiddleware,
]

schema = strawberry.Schema(
    query=Query,
    mutation=Mutations,
    extensions=extensions,

)

__all__ = [
    'schema',
    'Query',
    'Mutations',
]
