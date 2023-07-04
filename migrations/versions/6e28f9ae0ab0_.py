"""empty message

Revision ID: 6e28f9ae0ab0
Revises: 6b960c7e4382
Create Date: 2023-07-03 17:42:19.319023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e28f9ae0ab0'
down_revision = '6b960c7e4382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe_steps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_steps')
    # ### end Alembic commands ###
