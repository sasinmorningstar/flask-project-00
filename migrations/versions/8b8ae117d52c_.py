"""empty message

Revision ID: 8b8ae117d52c
Revises: c34c629e0599
Create Date: 2021-03-02 17:56:53.963611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b8ae117d52c'
down_revision = 'c34c629e0599'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    # ### end Alembic commands ###