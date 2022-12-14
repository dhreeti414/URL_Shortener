"""First Migration

Revision ID: 784a15f1ab6e
Revises: 
Create Date: 2022-08-15 20:34:30.716235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784a15f1ab6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('long_url', sa.Text(), nullable=True),
    sa.Column('short_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    # ### end Alembic commands ###
