"""change db name

Revision ID: 48d4f8401f4d
Revises: 0f89266ff6b6
Create Date: 2025-03-05 20:44:41.621784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel    
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '48d4f8401f4d'
down_revision: Union[str, None] = '0f89266ff6b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('full_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('uid', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('publisher', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('published_date', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('page_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('language', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('uid', name='book_pkey')
    )
    op.create_table('user',
    sa.Column('uid', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('uid', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
