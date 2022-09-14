from typing import Optional

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


@strawberry.input
class FlightUpdateInput:
    id: strawberry.ID
    airline: Optional[int] = None
    flight_number: Optional[str] = None
    departure: Optional[str] = None
    arrival: Optional[str] = None
    departure_time: Optional[str] = None
    arrival_time: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None


@strawberry.input
class AirlineInput:
    name: str
    # logo: str
    website: Optional[str] = None
    country: Optional[str] = None
    slogan: Optional[str] = None
    head_quaters: Optional[str] = None
    established: Optional[str] = None
    is_active: Optional[bool] = None



__all__ = [
    "FlightInput",
    "AirlineInput",
    "FlightUpdateInput",
]
