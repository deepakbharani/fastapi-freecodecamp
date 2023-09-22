"""add new column to the supplier_tab

Revision ID: 5d4def41e6d2
Revises: e18c0681110c
Create Date: 2023-09-19 11:17:01.469075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d4def41e6d2'
down_revision: Union[str, None] = 'e18c0681110c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('supplier_table', 
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                  )
        #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #owner_id = Column(Integer, ForeignKey("users_table.id", ondelete="CASCADE"), nullable=False)
    #owner = relationship("User")
    pass                
#                    sa.PrimaryKeyConstraint('id'),
#                    sa.UniqueConstraint('email')

def downgrade() -> None:
    op.drop_column('supplier_table','created_at')
    pass
