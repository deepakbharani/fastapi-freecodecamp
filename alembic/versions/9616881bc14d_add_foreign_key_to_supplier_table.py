"""add foreign key to supplier_table

Revision ID: 9616881bc14d
Revises: eee5347c91ca
Create Date: 2023-09-22 07:39:51.272882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9616881bc14d'
down_revision: Union[str, None] = 'eee5347c91ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('supplier_table',
                  sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key('supplier_users_fk', source_table="supplier_table", referent_table="users_table",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('supplier_users_fk', table_name="supplier_table")
    op.drop_column('supplier_table', 'owner_id')
    pass