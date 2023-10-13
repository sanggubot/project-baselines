from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="project-baselines/python-devcontainer-fastapi",
    version="0.1.0",
    # redoc_url=None,
    # docs_url=None,
)

class Item(BaseModel):
    id: str
    value: str

class Message(BaseModel):
    message: str


@app.get(
    path="/items/{item_id}",
    description="get item",
    response_model=Item,
    responses={
        404: {"model": Message, "description": "The item was not found"},
        200: {
            "description": "Item requested by ID",
            "content": {
                "application/json": {
                    "example": {"id": "bar", "value": "The bar tenders"}
                }
            },
        },
    },
)
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    return JSONResponse(status_code=404, content={"message": "Item not found"})
