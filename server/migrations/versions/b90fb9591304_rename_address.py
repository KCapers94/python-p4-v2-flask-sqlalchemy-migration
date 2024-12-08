"""rename address

Revision ID: b90fb9591304
Revises: 8150d736e3a3
Create Date: 2024-12-07 22:24:17.183281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b90fb9591304'
down_revision = '8150d736e3a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name= 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###
