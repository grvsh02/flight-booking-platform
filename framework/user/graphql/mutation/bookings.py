from typing import List

import strawberry
from strawberry_django_jwt.decorators import login_required

from user.graphql.inputs.booking import FlightBookingInput, PassengerInput


@strawberry.type
class BookingMutations:

    @strawberry.mutation
    @login_required
    def book_flight(
            self, info,
            booking: FlightBookingInput,
            passengers: List[PassengerInput],
    ) -> bool:

        from user.models.bookings import Bookings
        from user.models.user import User
        from flights.models.flights import Flights
        from user.models.passengers import Passengers
        try:
            User.objects.get(id=booking.user)
        except User.DoesNotExist:
            raise ValueError("User does not exist")
        try:
            flight = Flights.objects.get(id=booking.flight)
        except Flights.DoesNotExist:
            raise ValueError("Flight does not exist")

        amount = flight.price * len(passengers)

        if flight.is_active:
            user = User.objects.get(id=booking.user)
            flight = Flights.objects.get(id=booking.flight)
            booking = Bookings.objects.create(
                user=user,
                flight=flight,
                date=booking.date,
                amount=amount,
            )
        else:
            raise ValueError("Flight is not active")

        for passenger in passengers:
            passenger = Passengers.objects.create(
                first_name=passenger.first_name,
                last_name=passenger.last_name,
                booking=booking,
                age=passenger.age,
            )

        return True
