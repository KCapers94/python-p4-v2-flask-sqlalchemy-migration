"""rename department

Revision ID: 8150d736e3a3
Revises: 56f04466eaea
Create Date: 2024-12-07 18:07:10.740648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8150d736e3a3'
down_revision = '56f04466eaea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department','departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments','department')
    # ### end Alembic commands ###
