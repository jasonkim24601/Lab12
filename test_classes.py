import pytest
from classes import *


def test_default():
    tv_default = Television()
    assert tv_default.tv_channel == 0
    assert tv_default.tv_volume == 0
    assert tv_default.tv_status == False


def test_power():
    tv_powerTest = Television()
    tv_powerTest.power()
    assert tv_powerTest.tv_status == True
    tv_powerTest.power()
    assert tv_powerTest.tv_status == False


def test_channel():
    tv_channelTest = Television()
    tv_channelTest.channel_up()
    assert tv_channelTest.tv_channel == 1

    # assert tv_channeltest.tv_channel == 0
    # tv_channeltest.channel_up()
    # assert tv_channeltest.tv_channel == 2
    # tv_channeltest.channel_up()
    # assert tv_channeltest.tv_channel == 3
    # tv_channeltest.channel_up()
    # assert tv_channeltest.tv_channel == 0

    # tv_channeltest.channel_down()
    # assert tv_channeltest.tv_channel == 3
    # tv_channeltest.channel_down()
    # assert tv_channeltest.tv_channel == 2
    # tv_channeltest.channel_down()
    # assert tv_channeltest.tv_channel == 1
    # tv_channeltest.channel_down()
    # assert tv_channeltest.tv_channel == 0
