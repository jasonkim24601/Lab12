class Television:
    """
    A class representing details for a Television Object
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel
    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        """
        Constructor to create a Television Object with default states.
        :param tv_channel: Current TV channel, initialized as MIN_CHANNEL, can be adjusted up to MAX_CHANNEL
        :param tv_volume: Current TV volume, initialized as MIN_VOLUME, can be adjusted up to MAX_VOLUME
        :param tv_status: Current TV Status, initialized as False. Television object is considered ON when True, OFF when False.
        """
        self.tv_channel = Television.MIN_CHANNEL
        self.tv_volume = Television.MIN_VOLUME
        self.tv_status = False

    def power(self):
        """
        Method to change TV Status, if it's True, set to False and vice versa.
        """
        if self.tv_status == False:
            self.tv_status = True
        else:
            self.tv_status = False

    def channel_up(self):
        """
        Method to increase tv_channel up one channel, or if it is equal to MAX_CHANNEL, sets it to MIN_CHANNEL
        """
        if self.tv_status == True:
            if self.tv_channel != Television.MAX_CHANNEL:
                self.tv_channel = self.tv_channel + 1
            else:
                self.tv_channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease tv_channel down one channel, or if it is equal to MIN_CHANNEL, sets it to MAX_CHANNEL
        """
        if self.tv_status == True:
            if self.tv_channel == Television.MAX_CHANNEL:
                self.tv_channel = Television.MIN_CHANNEL
            else:
                self.tv_channel = self.tv_channel - 1

    def volume_up(self):
        """
        Method to increase tv_volume by 1 assuming that it isn't currently equal to MAX_VOLUME
        """
        if self.tv_status == True:
            if self.tv_volume != Television.MAX_VOLUME:
                self.tv_volume = self.tv_volume + 1

    def volume_down(self):
        """
        Method to decrease tv_volume by 1 assuming that it isn't currently equal to MIN_VOLUME
        """
        if self.tv_status == True:
            if self.tv_volume != Television.MIN_VOLUME:
                self.tv_volume = self.tv_volume - 1

    def __str__(self):
        """
        Method to return current Television Object's status
        :return: A string in the form of: "TV status: Is on = True/False, Channel = tv_channel, Volume = tv_volume"
        """
        tv_statusString = ""
        if self.tv_status == False:
            tv_statusString = "False"
        else:
            tv_statusString = "True"

        returnString = ("TV status: Is on = %s, Channel = %d, Volume = %d" % (
            tv_statusString, self.tv_channel, self.tv_volume))
        return returnString

    def returnChannel(self):
        """
        Method to return the current channel.
        :return: tv_channel
        """
        return self.tv_channel
    def returnVolume(self):
        """
        Method to return the current volume.
        :return: tv_volume
        """
        return self.tv_volume