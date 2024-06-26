"""Adding in "allow_self_join" column to enable self join in dispatch UI

Revision ID: a836d4850a75
Revises: b07bb852fd67
Create Date: 2024-04-29 10:28:37.777618

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a836d4850a75'
down_revision = 'b07bb852fd67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('allow_self_join', sa.Boolean(), server_default='t', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'allow_self_join')
    # ### end Alembic commands ###
