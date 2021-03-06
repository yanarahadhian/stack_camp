"""empty message

Revision ID: ad8ac826816a
Revises: 
Create Date: 2019-01-09 11:17:50.467535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad8ac826816a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_v2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user')
    op.drop_constraint(None, 'token_blacklist', type_='foreignkey')
    op.create_foreign_key(None, 'token_blacklist', 'user_v2', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'token_blacklist', type_='foreignkey')
    op.create_foreign_key(None, 'token_blacklist', 'user', ['user_id'], ['id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), nullable=False),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('active IN (0, 1)'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user_v2')
    # ### end Alembic commands ###
