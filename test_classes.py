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
    # Test to make sure TV doesn't change channel while television is off
    tv_channelTest.channel_up()
    assert tv_channelTest.tv_channel == 0
    tv_channelTest.power()
    tv_channelTest.channel_up()
    assert tv_channelTest.tv_channel == 1
    tv_channelTest.channel_up()
    assert tv_channelTest.tv_channel == 2
    tv_channelTest.channel_up()
    assert tv_channelTest.tv_channel == 3
    tv_channelTest.channel_up()
    assert tv_channelTest.tv_channel == 0
    # Test to make sure TV doesn't change channel while television is off
    tv_channelTest.power()
    tv_channelTest.channel_down()
    assert tv_channelTest.tv_channel == 0
    tv_channelTest.power()
    tv_channelTest.channel_down()
    assert tv_channelTest.tv_channel == 3
    tv_channelTest.channel_down()
    assert tv_channelTest.tv_channel == 2
    tv_channelTest.channel_down()
    assert tv_channelTest.tv_channel == 1
    tv_channelTest.channel_down()
    assert tv_channelTest.tv_channel == 0


def test_volume():
    tv_volumeTest = Television()
    # Test to make sure volume cannot increase while television is off
    tv_volumeTest.volume_up()
    assert tv_volumeTest.tv_volume == 0
    tv_volumeTest.power()
    tv_volumeTest.volume_up()
    assert tv_volumeTest.tv_volume == 1
    tv_volumeTest.volume_up()
    assert tv_volumeTest.tv_volume == 2
    # Make sure that volume can't exceed max
    tv_volumeTest.volume_up()
    assert tv_volumeTest.tv_volume == 2
    # Test to make sure volume cannot decrease while television is off
    tv_volumeTest.power()
    tv_volumeTest.volume_down()
    assert tv_volumeTest.tv_volume == 2
    tv_volumeTest.power()
    tv_volumeTest.volume_down()
    assert tv_volumeTest.tv_volume == 1
    tv_volumeTest.volume_down()
    assert tv_volumeTest.tv_volume == 0
    tv_volumeTest.volume_down()
    assert tv_volumeTest.tv_volume == 0


def test_print():
    tv_printTest = Television()
    assert str(tv_printTest) == "TV status: Is on = False, Channel = 0, Volume = 0"
    tv_printTest.power()
    tv_printTest.channel_up()
    tv_printTest.volume_up()
    assert str(tv_printTest) == "TV status: Is on = True, Channel = 1, Volume = 1"