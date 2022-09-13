import strawberry

from flights.graphql.inputs import FlightInput
from flights.graphql.types import FlightType


@strawberry.type
class FlightMutations:

    @strawberry.mutation
    def create_flight(
            self, info,
            flight: FlightInput,
    ) -> FlightType:
        from flights.models.flights import Flights
        flight = Flights.objects.create(
            airline_id=flight.airline,
            flight_number=flight.flight_number,
            departure=flight.departure,
            arrival=flight.arrival,
            departure_time=flight.departure_time,
            arrival_time=flight.arrival_time,
            price=flight.price,
            is_active=flight.is_active,
        )
        return flight
