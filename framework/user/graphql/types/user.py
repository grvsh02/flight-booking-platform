import strawberry


@strawberry.type
class UserType:
    id: int
    first_name: str
    last_name: str
    email: str
    is_active: bool

__all__ = [
    "UserType",
]
