import allure
import pytest


def test_a():
    print('aaaa\n')
    assert 1
@allure.step(title= '测试登陆的流程')
def test_b():
    allure.attach('登陆', '输入用户名')
    print('bbbb\n')
    allure.attach('登陆', '输入密码')
    print('bbbb\n')
    allure.attach('登陆', '点击登陆')
    print('bbbb\n')
    assert 1


