import strawberry
from strawberry.extensions import QueryDepthLimiter, ValidationCache, ParserCache, AddValidationRules
from strawberry.tools import merge_types
from flights.graphql.mutations import FlightMutations
from flights.graphql.queries import FlightQueries

Mutations = merge_types('Mutations', (FlightMutations,))
Query = merge_types('Queries', (FlightQueries,))

extensions = [
    QueryDepthLimiter(max_depth=10),
    ParserCache(maxsize=100),
    ValidationCache(maxsize=100),
]

schema = strawberry.Schema(
    query=Query,
    mutation=Mutations,
    extensions=extensions
)

__all__ = [
    'schema',
    'Query',
    # 'Mutations',
]
