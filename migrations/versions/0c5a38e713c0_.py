"""empty message

Revision ID: 0c5a38e713c0
Revises: 88ca2ab86625
Create Date: 2022-09-18 22:42:13.242146

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0c5a38e713c0'
down_revision = '88ca2ab86625'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('permission', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
