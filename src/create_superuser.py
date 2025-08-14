import asyncio

from src.users.models import User

from .database import AsyncSessionLocal


async def create_superuser():
    async with AsyncSessionLocal() as session:
        user = User(
            username='admin',
            hashed_password='admin',
            email='admin@admin.admin',
            is_superuser=True,
            is_verified=True,
        )
        session.add(user)
        await session.commit()
        print('Superuser created.')


if __name__ == '__main__':
    asyncio.run(create_superuser())
