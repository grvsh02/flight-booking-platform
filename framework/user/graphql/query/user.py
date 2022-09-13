import strawberry

from user.graphql.types.user import UserType


@strawberry.type
class UserQueries:

        @strawberry.field
        def view_user(
                self, info,
                userId: int
        ) -> UserType:
            from user.models.user import User
            qs = User.objects.all()
            try:
                qs = qs.filter(id=userId)
                return qs
            except User.DoesNotExist:
                raise ValueError("User does not exit")