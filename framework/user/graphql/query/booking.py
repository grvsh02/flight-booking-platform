from typing import List

import strawberry

from user.graphql.types.booking import BookingType, BookingsType


@strawberry.type
class BookingQueries:

    @strawberry.field
    def view_bookings(
            self, info,
            userId: int
    ) -> List[BookingsType]:
        from user.models.user import User
        try:
            user = User.objects.get(id=userId)
        except User.DoesNotExist:
            raise ValueError("User does not exist")
        from user.models.bookings import Bookings

        qs = Bookings.objects.filter(user_id=userId)

        return qs

    @strawberry.field
    def view_booking(
            self, info,
            userId: int,
            bookingId: int
    ) -> BookingType:
        from user.models.user import User
        try:
            user = User.objects.get(id=userId)
        except User.DoesNotExist:
            raise ValueError("User does not exist")
        from user.models.bookings import Bookings
        try:
            booking = Bookings.objects.get(id=bookingId)
        except Bookings.DoesNotExist:
            raise ValueError("Booking does not exist")
        if booking.user_id != userId:
            raise ValueError("Booking does not belong to user")

        from user.models.passengers import Passengers
        passengers = Passengers.objects.filter(booking_id=bookingId)

        return BookingType(
            booking=booking,
            passengers=passengers
        )
