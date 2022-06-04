import pytest

from src.domain.entities.grade import Grade
from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.helpers.errors.domain_errors import EntityError


class Test_Grade:

    def test_grade(self):
        grade = Grade(
                        value=3.0,
                        evaluationType=EVALUATION_TYPE.P1,
                        weight=0.2
                    )

        assert type(grade) == Grade

    async def test_grade_entity_error(self):
        with pytest.raises(EntityError):
            await Grade(value='',
                          evaluationType='',
                          weight='')
