"""Create Post table

Revision ID: e18c0681110c
Revises: 
Create Date: 2023-09-18 16:15:02.869788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e18c0681110c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('supplier_table', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(),nullable=False),
                    sa.Column('address', sa.String(),nullable=False),
                    sa.Column('email', sa.String()),
                    sa.Column('phone', sa.String(),nullable=False),
                    sa.Column('vat_no', sa.String(),nullable=False))

    pass
    #id = Column(Integer, primary_key=True, nullable=False)
    #name = Column(String, nullable=False)
    #address = Column(String, nullable=False)
    #email = Column(String)
    #phone = Column(String, nullable=False)
    #vat_no = Column(String, nullable=False)


def downgrade():
    op.drop_table('supplier_table')
    
    pass
