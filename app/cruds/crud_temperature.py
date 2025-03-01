from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.models.temperature import Temperature
from app.schemas.temperature import TemperatureBase



async def get_all_temperatures(
        db: AsyncSession, skip: int = 0, limit: int = 10, city_id: int = None
) -> list[Temperature]:
    """
    Retrieve a list of temperature records from the database.

    Args:
        db (AsyncSession): Database session.
        skip (int): Number of records to skip (for pagination).
        limit (int): Maximum number of records to return.
        city_id (int): If provided, filter temperature records by city ID.

    Returns:
        list[Temperature]: List of temperature records.
    """
    query = select(Temperature).offset(skip).limit(limit)
    if city_id:
        query = select(Temperature).where(Temperature.city_id == city_id).offset(skip).limit(limit)

    result = await db.execute(query)
    temperatures = result.scalars().all()
    return temperatures


async def get_temperature_by_id(db: AsyncSession, temperature_id: int) -> Temperature:
    """
    Retrieve a specific temperature record by its ID.

    Args:
        db (AsyncSession): Database session.
        temperature_id (int): ID of the temperature record.

    Returns:
        Temperature: The temperature instance.
    """
    result = await db.execute(select(Temperature).where(Temperature.id == temperature_id))
    temperature = result.scalar_one_or_none()
    if not temperature:
        raise NoResultFound(f"Temperature record with id {temperature_id} does not exist.")
    return temperature
