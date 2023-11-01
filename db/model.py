from sqlalchemy import Column, Integer, String, Enum, ARRAY, TIMESTAMP, UUID, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Todo: Need to solve upgrade detect error

# ERROR [alembic.util.messaging] New upgrade operations detected: [('add_table', Table('public.user_details', MetaData(), Column('user_id', UUID(), table=<public.user_details>, primary_key=True, nullable=False), Column('created_at', TIMESTAMP(timezone=True), table=<public.user_details>), Column('first_name', VARCHAR(length=255), table=<public.user_details>), Column('last_name', VARCHAR(length=255), table=<public.user_details>), Column('phone_number', VARCHAR(length=31), table=<public.user_details>), Column('country', VARCHAR(length=31), table=<public.user_details>), Column('country_code', VARCHAR(length=15), table=<public.user_details>), Column('profile_image', VARCHAR(length=255), table=<public.user_details>), Column('cover_video', ARRAY(UUID()), table=<public.user_details>), schema=None))]
#   FAILED: New upgrade operations detected: [('add_table', Table('public.user_details', MetaData(), Column('user_id', UUID(), table=<public.user_details>,
#   primary_key=True, nullable=False), Column('created_at', TIMESTAMP(timezone=True), table=<public.user_details>), Column('first_name',
#   VARCHAR(length=255), table=<public.user_details>), Column('last_name', VARCHAR(length=255), table=<public.user_details>), Column('phone_number',
#   VARCHAR(length=31), table=<public.user_details>), Column('country', VARCHAR(length=31), table=<public.user_details>), Column('country_code',
#   VARCHAR(length=15), table=<public.user_details>), Column('profile_image', VARCHAR(length=255), table=<public.user_details>), Column('cover_video',
#   ARRAY(UUID()), table=<public.user_details>), schema=None))]

# Possible solution: solving schema setting error / seems like schema is not recorded

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