"""Change image field to store URL

Revision ID: a277aba88f7c
Revises: c5df429633ac
Create Date: 2025-03-25 21:14:53.586264

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a277aba88f7c'
down_revision = 'c5df429633ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=mysql.LONGBLOB(),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.String(length=255),
               type_=mysql.LONGBLOB(),
               existing_nullable=True)

    # ### end Alembic commands ###
