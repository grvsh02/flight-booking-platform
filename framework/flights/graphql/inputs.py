import strawberry


@strawberry.input
class FlightInput:
    airline: int
    flight_number: str
    departure: str
    arrival: str
    departure_time: str
    arrival_time: str
    price: float
    is_active: bool


__all__ = [
    "FlightInput",
]
