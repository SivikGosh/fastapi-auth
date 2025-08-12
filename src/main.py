from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import get_async_db
from .users import router as users_router

app = FastAPI()
app.include_router(users_router)


@app.get('/')
async def init(db: AsyncSession = Depends(get_async_db)):
    try:
        await db.execute(text('SELECT 1'))
        return {'database': 'reachable'}
    except Exception as e:
        raise HTTPException(
            status.HTTP_418_IM_A_TEAPOT,
            f'Сonnection error: {e}'
        )
