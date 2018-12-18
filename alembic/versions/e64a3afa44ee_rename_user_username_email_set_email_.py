"""Rename User.username => email, set email/password field lengths to 256

Revision ID: e64a3afa44ee
Revises: 17253afc4adf
Create Date: 2018-12-08 08:49:29.233745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e64a3afa44ee'
down_revision = '17253afc4adf'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'username', new_column_name='email')
    op.alter_column('users', 'email', type_=sa.Column(sa.String(256)))
    op.alter_column('users', 'password', type_=sa.Column(sa.String(256)))

def downgrade():
    op.alter_column('users', 'password', type_=sa.Column(sa.String()))
    op.alter_column('users', 'email', type_=sa.Column(sa.String()))
    op.alter_column('users', 'email', new_column_name='username')
