"""invoices table

Revision ID: cde07af54f5c
Revises: c9d892780522
Create Date: 2022-07-29 23:40:32.425028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cde07af54f5c'
down_revision = 'c9d892780522'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numer_faktury', sa.String(), nullable=True),
    sa.Column('sprzedawca', sa.String(length=64), nullable=True),
    sa.Column('nip_sprzedawcy', sa.Integer(), nullable=True),
    sa.Column('nabywca', sa.String(length=64), nullable=True),
    sa.Column('nip_nabywcy', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_invoice_nabywca'), 'invoice', ['nabywca'], unique=False)
    op.create_index(op.f('ix_invoice_sprzedawca'), 'invoice', ['sprzedawca'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_invoice_sprzedawca'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_nabywca'), table_name='invoice')
    op.drop_table('invoice')
    # ### end Alembic commands ###
