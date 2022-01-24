"""intial database

Revision ID: 357784aec51a
Revises: 
Create Date: 2022-01-19 20:54:09.070163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '357784aec51a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('create schema "Subject"')
    op.create_table('Subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codeSubject', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='Subject'
    )
    op.create_table('StudentSubjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idStudent', sa.Integer(), nullable=False),
    sa.Column('idSubject', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idSubject'], ['Subject.Subjects.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='Subject'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('drop schema "Subject"')
    op.drop_table('StudentSubjects', schema='Subject')
    op.drop_table('Subjects', schema='Subject')
    # ### end Alembic commands ###
