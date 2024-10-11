"""create pdfs table

Revision ID: 408d4f4f15e4
Revises: 0807b366c885
Create Date: 2024-10-11 21:26:46.716352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '408d4f4f15e4'
down_revision: Union[str, None] = '0807b366c885'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
