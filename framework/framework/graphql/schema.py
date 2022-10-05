import strawberry
from strawberry.extensions import QueryDepthLimiter, ValidationCache, ParserCache
from strawberry.tools import merge_types

from flights.graphql.mutations.airline import AirlineMutations
from flights.graphql.mutations.flight import FlightMutations
from flights.graphql.queries import FlightQueries
from user.graphql.mutation.bookings import BookingMutations
from user.graphql.query.booking import BookingQueries


Mutations = merge_types('Mutations', (FlightMutations, AirlineMutations, BookingMutations))
Query = merge_types('Queries', (FlightQueries, BookingQueries))

extensions = [
    QueryDepthLimiter(max_depth=10),
    ParserCache(maxsize=100),
    ValidationCache(maxsize=100),
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
