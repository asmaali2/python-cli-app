"""First Table

Revision ID: 653835264b7f
Revises: a386d01f150a
Create Date: 2024-01-11 10:59:28.747959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653835264b7f'
down_revision = 'a386d01f150a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts _id',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts _id')
    # ### end Alembic commands ###
