"""Table added

Revision ID: 6a956d8850c2
Revises:
Create Date: 2022-12-12 15:58:31.758895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6a956d8850c2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("competition", sa.Column("created_by", sa.TIMESTAMP(), nullable=True))
    op.add_column("competition", sa.Column("updated_by", sa.TIMESTAMP(), nullable=True))
    op.alter_column("competition", "name", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_column("competition", "is_active")
    op.add_column("entry", sa.Column("created_by", sa.TIMESTAMP(), nullable=True))
    op.add_column("entry", sa.Column("updated_by", sa.TIMESTAMP(), nullable=True))
    op.add_column("user", sa.Column("created_by", sa.TIMESTAMP(), nullable=True))
    op.add_column("user", sa.Column("updated_by", sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "updated_by")
    op.drop_column("user", "created_by")
    op.drop_column("entry", "updated_by")
    op.drop_column("entry", "created_by")
    op.add_column(
        "competition",
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.alter_column("competition", "name", existing_type=sa.VARCHAR(), nullable=False)
    op.drop_column("competition", "updated_by")
    op.drop_column("competition", "created_by")
    # ### end Alembic commands ###
