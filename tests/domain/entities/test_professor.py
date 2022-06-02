import pytest

from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError


class Test_Professor:

    def test_professor(self):
        prof = Professor(name="Ana Paula Gonçalves Serra",
                         email="ana.serra@maua.br",
                         phoneNumber="4239-3008")

        assert prof.name == "Ana Paula Gonçalves Serra"

    async def test_professor_entity_error(self):
        with pytest.raises(EntityError):
            await Professor(name='',
                            email='',
                            phoneNumber='')