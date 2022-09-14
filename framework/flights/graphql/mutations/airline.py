import strawberry
from strawberry_django_jwt.decorators import superuser_required

from flights.graphql.inputs import AirlineInput


@strawberry.type
class AirlineMutations:

    @strawberry.mutation
    @superuser_required
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
        if airline.logo and airline.logo is not None:
            airlineObj.logo = airline.logo
        if airline.website and airline.website is not None:
            airlineObj.website = airline.website
        if airline.slogan and airline.slogan is not None:
            airlineObj.slogan = airline.slogan
        if airline.headquarters and airline.headquarters is not None:
            airlineObj.headquarters = airline.headquarters
        if airline.established and airline.established is not None:
            airlineObj.established = airline.established
        if airline.country and airline.country is not None:
            airlineObj.country = airline.country
        return True

    @strawberry.mutation
    @superuser_required
    def update_airline(
            self, info,
            airline: AirlineInput,
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
        if airline.logo and airline.logo is not None:
            airlineObj.logo = airline.logo
        if airline.website and airline.website is not None:
            airlineObj.website = airline.website
        if airline.slogan and airline.slogan is not None:
            airlineObj.slogan = airline.slogan
        if airline.headquarters and airline.headquarters is not None:
            airlineObj.headquarters = airline.headquarters
        if airline.established and airline.established is not None:
            airlineObj.established = airline.established
        if airline.country and airline.country is not None:
            airlineObj.country = airline.country
        return True

    @strawberry.mutation
    @superuser_required
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