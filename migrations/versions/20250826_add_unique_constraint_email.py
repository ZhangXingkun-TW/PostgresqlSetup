"""Add unique constraint to users.email

Revision ID: 20250826_add_unique_constraint_email
Revises: de498970a5d7
Create Date: 2025-08-26 10:30:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20250826'
down_revision = 'de498970a5d7'  # 替换为上一个 migration 的 revision id
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration: add unique constraint."""
    op.create_unique_constraint(
        constraint_name="uq_users_email",  # 约束名
        table_name="users",                # 表名
        columns=["email"]                  # 需要约束的列
    )


def downgrade():
    """Rollback the migration: drop unique constraint."""
    op.drop_constraint(
        constraint_name="uq_users_email",
        table_name="users",
        type_="unique"
    )
