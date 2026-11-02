
import pytest


@pytest.fixture(scope="module")
def test_environment():
    print("\n[SETUP] 准备测试环境")

    yield "测试环境已准备好"

    print("\n[TEARDOWN] 清理测试环境")


def test_example_1(test_environment):
    print("[TEST] 执行第一条测试")
    assert test_environment == "测试环境已准备好"


def test_example_2(test_environment):
    print("[TEST] 执行第二条测试")
    assert 1 + 1 == 2
