"""added chef_id column in 'meals'

Revision ID: 8b9b35b2beeb
Revises: b4a31bee1caa
Create Date: 2019-01-30 09:39:24.998913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b9b35b2beeb'
down_revision = 'b4a31bee1caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meals', sa.Column('chef_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meals', 'chef_id')
    # ### end Alembic commands ###