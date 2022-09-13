import strawberry

@strawberry.input
class PassengerInput(strawberry.input):
    first_name: str
    last_name: str
    age: int
    gender: str


@strawberry.input
class FlightBookingInput:
    user: strawberry.ID
    flight: strawberry.ID
    date: str


__all__ = [
    "PassengerInput",
    "FlightBookingInput",
]