from typing import List, Optional

import strawberry

from flights.graphql.types import FlightType
from user.graphql.types.user import UserType


@strawberry.type
class PassengerType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int
    gender: Optional[str] = None


@strawberry.type
class BookingsType:
    id: strawberry.ID
    user: UserType
    flight: FlightType
    date: str
    amount: float


@strawberry.type
class BookingType:
    booking: BookingsType
    passengers: List[PassengerType]


__all__ = [
    "BookingType",
    "BookingsType",
    "PassengerType",
]
