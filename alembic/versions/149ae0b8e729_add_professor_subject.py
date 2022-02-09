"""add professor subject

Revision ID: 149ae0b8e729
Revises: 357784aec51a
Create Date: 2022-02-08 22:45:30.144389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '149ae0b8e729'
down_revision = '357784aec51a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ProfessorSubjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idProfessor', sa.Integer(), nullable=False),
    sa.Column('idSubject', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idSubject'], ['Subject.Subjects.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='Subject'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ProfessorSubjects', schema='Subject')
    # ### end Alembic commands ###