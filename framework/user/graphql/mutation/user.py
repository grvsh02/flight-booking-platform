import strawberry

from user.graphql.types.user import UserType


@strawberry.type
class UserMutations:

    @strawberry.mutation
    def signup(
            self, info,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
    ) -> UserType:
        from user.models.user import User
        try:
            user = User.objects.create(
                email=email)
        except:
            raise Exception("User already exists")
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return user
