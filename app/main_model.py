from pydantic import BaseModel, Field


class ItemsRequestModel(BaseModel):
    id: str = Field(title="id of item", description="id of item")

    class Config:
        json_schema_extra = {
            "examples": [
                {"id": "foo"},
                {"id": "bar"},
            ]
        }


class ItemsResponseModel(BaseModel):
    value: str = Field(title="value of item", description="value of item")

    class Config:
        json_schema_extra = {
            "examples": [
                {"value": "foofoo"},
                {"value": "barbar"},
            ]
        }
