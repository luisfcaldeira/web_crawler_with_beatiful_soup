
from abc import abstractmethod
import datetime


class LoggerProfile():

    @abstractmethod
    def red(self) -> int:
        pass

    @abstractmethod
    def green(self) -> int:
        pass

    @abstractmethod
    def blue(self) -> int:
        pass

class NormalLoggerProfile(LoggerProfile):

    def red(self) -> int:
        return 255

    def green(self) -> int:
        return 255

    def blue(self) -> int:
        return 255

class WarningLoggerProfile(LoggerProfile):

    def red(self) -> int:
        return 255

    def green(self) -> int:
        return 165

    def blue(self) -> int:
        return 0

class ErrorLoggerProfile(LoggerProfile):

    def red(self) -> int:
        return 255

    def green(self) -> int:
        return 0

    def blue(self) -> int:
        return 0

class InfoLoggerProfile(LoggerProfile):

    def red(self) -> int:
        return 0

    def green(self) -> int:
        return 255

    def blue(self) -> int:
        return 255

class ConsoleLogger():

    def __init__(self) -> None:
        self.__now = datetime.datetime.now()

    def __colored(self, r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    def log_this(self, msg=None, print_diff = False, profile=None):
        new_now = datetime.datetime.now()
        
        if profile == None:
            profile = NormalLoggerProfile()

        str_now = new_now.strftime(r'%Y-%m-%d %H:%M:%S')
        print(self.__colored(profile.red(), profile.green(), profile.blue(), str_now), end=' ')

        if print_diff:
            diff = (new_now - self.__now).microseconds
            print(self.__colored(profile.red(), profile.green(), profile.blue(), diff), end=' ')

        if msg != None:
            print(self.__colored(profile.red(), profile.green(), profile.blue(), msg), end=' ')
        
        self.__now = new_now

        print('')