"""empty message

Revision ID: 50f3efafc212
Revises: 09a1c989cc44
Create Date: 2020-05-12 22:35:27.208840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f3efafc212'
down_revision = '09a1c989cc44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('users', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uid', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('users', 'id')
    # ### end Alembic commands ###