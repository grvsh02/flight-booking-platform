from typing import Optional

import strawberry


@strawberry.input
class PassengerInput:
    first_name: str
    last_name: str
    age: int
    gender: Optional[str] = None


@strawberry.input
class FlightBookingInput:
    user: strawberry.ID
    flight: strawberry.ID
    date: str


__all__ = [
    "PassengerInput",
    "FlightBookingInput",
]
