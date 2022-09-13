from typing import Optional

import strawberry
from django.core.paginator import Paginator

from flights.graphql.types import FlightsType, FlightType


@strawberry.type
class FlightQueries:

    @strawberry.field
    def flights(
            self, info,
            per_page: Optional[int] = 10,
            page_no: Optional[int] = 1,
    ) -> FlightsType:
        from flights.models.flights import Flights
        qs = Flights.objects.all()

        paginator = Paginator(qs, per_page)

        return FlightsType(
            flights=paginator.page(page_no).object_list,
            totalCount=paginator.count,
            pages=paginator.num_pages,
        )

    @strawberry.field
    def flight(
            self, info,
            id: strawberry.ID
    ) -> FlightType:
        from flights.models.flights import Flights
        return Flights.objects.get(id=id)