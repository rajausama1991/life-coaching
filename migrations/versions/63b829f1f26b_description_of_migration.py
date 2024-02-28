"""description_of_migration

Revision ID: 63b829f1f26b
Revises: 7838ad59e7de
Create Date: 2023-09-08 16:57:04.777505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63b829f1f26b'
down_revision = '7838ad59e7de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booked_slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('appointment_id', sa.Integer(), nullable=False),
    sa.Column('booking_time', sa.DateTime(), nullable=False),
    sa.Column('user_email', sa.String(length=100), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['appointment_id'], ['appointment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_time', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('end_time', sa.DateTime(), nullable=False))
        batch_op.drop_column('email')
        batch_op.drop_column('date')
        batch_op.drop_column('payment_status')
        batch_op.drop_column('full_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_name', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('payment_status', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('date', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('end_time')
        batch_op.drop_column('start_time')

    op.drop_table('booked_slot')
    # ### end Alembic commands ###
