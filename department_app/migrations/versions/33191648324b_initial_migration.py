"""Initial migration.

Revision ID: 33191648324b
Revises: 
Create Date: 2021-12-05 19:09:36.366317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33191648324b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    op.drop_table('departments')
    # ### end Alembic commands ###
