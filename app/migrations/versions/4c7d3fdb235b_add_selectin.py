"""add selectin

Revision ID: 4c7d3fdb235b
Revises: 71955d788cc8
Create Date: 2025-03-09 20:18:45.262032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel    


# revision identifiers, used by Alembic.
revision: str = '4c7d3fdb235b'
down_revision: Union[str, None] = '71955d788cc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
