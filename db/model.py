from sqlalchemy import Column, Integer, String, Enum, ARRAY, TIMESTAMP, UUID, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserDetails(Base):
    __tablename__ = 'public.user_details'  # Specify the schema and table name

    user_id = Column(UUID, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    first_name = Column(VARCHAR(length=255), nullable=True)
    last_name = Column(VARCHAR(length=255), nullable=True)
    phone_number = Column(VARCHAR(length=31), nullable=True)
    country = Column(VARCHAR(length=31), nullable=True)
    country_code = Column(VARCHAR(length=15), nullable=True)
    profile_image = Column(VARCHAR(length=255), nullable=True)  # Assuming it's a URL
    cover_video = Column(ARRAY(UUID), nullable=True)  # Assuming it's a list of IDs