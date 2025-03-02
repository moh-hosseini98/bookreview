from sqlmodel import SQLModel,Field

class ItemBase(SQLModel):
    title : str
    description : str | None = None

class ItemCreate(ItemBase):
    pass

class Item(SQLModel,table=True):

    __tablenname__ = "items"
    
    id : int = Field(primary_key=True,nullable=False)