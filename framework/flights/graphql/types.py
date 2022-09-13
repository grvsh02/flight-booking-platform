from typing import List

import strawberry


@strawberry.type
class AirlineType:
    id: int
    name: str
    # logo: str
    website: str
    country: str
    slogan: str
    head_quaters: str
    established: str
    is_active: bool


@strawberry.type
class FlightType:
    id: strawberry.ID
    airline: AirlineType
    flight_number: str
    departure: str
    arrival: str
    departure_time: str
    arrival_time: str
    price: float
    is_active: bool


@strawberry.type
class FlightsType:
    flights: List[FlightType]
    totalCount: int
    pages: int


__all__ = [
    "FlightType",
    "FlightsType",
]
