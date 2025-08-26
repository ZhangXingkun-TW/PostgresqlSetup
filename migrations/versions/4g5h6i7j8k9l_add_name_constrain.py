"""Add CHECK constraint to users.name"""

from alembic import op

# revision identifiers
revision = '4g5h6i7j8k9l'
down_revision = '20250826'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        ALTER TABLE users
        ADD CONSTRAINT chk_users_name_not_null
        CHECK (name IS NOT NULL);
    """)


def downgrade():
    op.execute("""
        ALTER TABLE users
        DROP CONSTRAINT chk_users_name_not_null;
    """)
