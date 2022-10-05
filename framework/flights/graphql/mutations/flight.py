import strawberry

from flights.graphql.inputs import FlightInput, FlightUpdateInput
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

    @strawberry.mutation
    def update_flight(
            self, info,
            flight: FlightUpdateInput,
    ) -> FlightType:
        from flights.models.flights import Flights
        flight = Flights.objects.get(id=flight.id)
        if flight is None:
            raise ValueError("Flight does not exist")
        if flight.flight_number and flight.flight_number is not None:
            flight.flight_number = flight.flight_number
        if flight.departure and flight.departure is not None:
            flight.departure = flight.departure
        if flight.arrival and flight.arrival is not None:
            flight.arrival = flight.arrival
        if flight.departure_time and flight.departure_time is not None:
            flight.departure_time = flight.departure_time
        if flight.arrival_time and flight.arrival_time is not None:
            flight.arrival_time = flight.arrival_time
        if flight.price and flight.price is not None:
            flight.price = flight.price
        if flight.is_active and flight.is_active is not None:
            flight.is_active = flight.is_active
        flight.save()
        return flight

    @strawberry.mutation
    def delete_flight(
            self, info,
            flight_id: int,
    ) -> bool:
        from flights.models.flights import Flights
        flight = Flights.objects.get(id=flight_id)
        if flight is None:
            raise ValueError("Flight does not exist")
        flight.delete()
        return True
