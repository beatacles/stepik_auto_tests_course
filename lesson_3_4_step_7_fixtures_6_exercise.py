import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")#1
    yield
    print(":3", "\n")#2


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")#3


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")#4,5


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print("ok")

    def test_second_smiling_faces(self, prepare_faces):
        print("ok")