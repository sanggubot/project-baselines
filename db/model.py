from sqlalchemy import Column, ARRAY, TIMESTAMP, UUID, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserDetails(Base):
    __tablename__ = 'user_details'  # Specify the schema and table name
    __table_args__ = {'schema': 'public'}

    user_id = Column(UUID, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    first_name = Column(VARCHAR(length=255), nullable=True)
    last_name = Column( VARCHAR(length=255), nullable=True)
    phone_number = Column(VARCHAR(length=31), nullable=True)
    country = Column(VARCHAR(length=31), nullable=True)
    country_code = Column(VARCHAR(length=15), nullable=True)
    profile_image = Column(VARCHAR(length=255), nullable=True)  # Assuming it's a URL
    cover_video = Column(ARRAY(UUID), nullable=True)  # Assuming it's a list of IDs