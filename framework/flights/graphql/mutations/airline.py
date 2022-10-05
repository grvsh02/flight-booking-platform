import strawberry

from flights.graphql.inputs import AirlineInput, AirlineUpdateInput


@strawberry.type
class AirlineMutations:

    @strawberry.mutation
    def create_airline(
            self, info,
            airline: AirlineInput,
    ) -> bool:
        from flights.models.airlines import Airlines
        airlineObj = Airlines.objects.create(
            name=airline.name,
        )

        if airline.website and airline.website is not None:
            airlineObj.website = airline.website
        if airline.website and airline.website is not None:
            airlineObj.website = airline.website
        if airline.slogan and airline.slogan is not None:
            airlineObj.slogan = airline.slogan
        if airline.established and airline.established is not None:
            airlineObj.established = airline.established
        if airline.country and airline.country is not None:
            airlineObj.country = airline.country
        airlineObj.save()
        return True

    @strawberry.mutation
    def update_airline(
            self, info,
            airline: AirlineUpdateInput,
    ) -> bool:
        from flights.models.airlines import Airlines
        try:
            airlineObj = Airlines.objects.get(id=airline.id)
        except Airlines.DoesNotExist:
            raise ValueError("Airline does not exist")

        if airline.name and airline.name is not None:
            airlineObj.name = airline.name
        if airline.website and airline.website is not None:
            airlineObj.website = airline.website
        if airline.website and airline.website is not None:
            airlineObj.website = airline.website
        if airline.slogan and airline.slogan is not None:
            airlineObj.slogan = airline.slogan
        if airline.established and airline.established is not None:
            airlineObj.established = airline.established
        if airline.country and airline.country is not None:
            airlineObj.country = airline.country
        airlineObj.save()
        return True

    @strawberry.mutation
    def delete_airline(
            self, info,
            airline_id: int,
    ) -> bool:
        from flights.models.airlines import Airlines
        try:
            airlineObj = Airlines.objects.get(id=airline_id)
        except Airlines.DoesNotExist:
            raise ValueError("Airline does not exist")
        airlineObj.delete()
        return True