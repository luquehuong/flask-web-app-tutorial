"""follower

Revision ID: 06defe811414
Revises: 4392fa1e14f6
Create Date: 2019-05-21 15:20:02.140834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06defe811414'
down_revision = '4392fa1e14f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###