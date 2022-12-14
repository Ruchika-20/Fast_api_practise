"""Table added

Revision ID: 15408814a32e
Revises: 6a956d8850c2
Create Date: 2022-12-12 16:10:20.969050

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "15408814a32e"
down_revision = "6a956d8850c2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("competition", "updated_by")
    op.drop_column("competition", "created_by")
    op.drop_column("entry", "updated_by")
    op.drop_column("entry", "created_by")
    op.drop_column("user", "updated_by")
    op.drop_column("user", "created_by")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column(
            "created_by", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "user",
        sa.Column(
            "updated_by", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "entry",
        sa.Column(
            "created_by", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "entry",
        sa.Column(
            "updated_by", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "competition",
        sa.Column(
            "created_by", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "competition",
        sa.Column(
            "updated_by", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    # ### end Alembic commands ###
