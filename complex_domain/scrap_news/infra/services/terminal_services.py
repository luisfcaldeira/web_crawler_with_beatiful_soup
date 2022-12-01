
from abc import ABC, abstractmethod, abstractproperty
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

class CallbackExecution(ABC):

    @abstractmethod
    def execute(self, user_response: str) -> None:
        pass

class ConsoleCommand(ABC):

    @abstractproperty
    def what_i_do(self) -> str:
        pass

    @abstractproperty
    def which_is_my_key(self) -> str:
        pass

    @abstractmethod
    def is_command(self, input_str: str) -> bool:
        pass

    @abstractmethod
    def proceed(self, user_response: str) -> None:
        pass

class ExitCommand(ConsoleCommand):

    def __init__(self, callback_execution: CallbackExecution) -> None:
        self.__callback_execution = callback_execution

    @property
    def what_i_do(self) -> str:
        return "exit"

    @property
    def which_is_my_key(self) -> str:
        return "0 or 'exit'"

    def is_command(self, input_str: str) -> bool:
        return input_str == 'exit' or input_str == '0'

    def proceed(self, user_response: str) -> None:
        self.__callback_execution.execute(user_response=user_response)

    def __eq__(self, __o: object) -> bool:
        return self.which_is_my_key.__eq__(__o.which_is_my_key)

class ExitCallbackExecution(CallbackExecution):

    def execute(self, user_response: str) -> None:
        exit()

class ConsoleReader():

    def __init__(self) -> None:
        self.__expected_commands = [
            ExitCommand(ExitCallbackExecution())
        ]

    def read_input(self):
        self.__print_options()

        input_str = input()

        self.__check_if_its_a_command(input_str)

    def __print_options(self):
        self.__expected_commands.sort()
        for expected_command in self.__expected_commands:
            print(expected_command.which_is_my_key, '- for ', expected_command.what_i_do)

    def __check_if_its_a_command(self, input_str) -> None:
        for expected_command in self.__expected_commands:
            if expected_command.is_command(input_str=input_str):
                expected_command.proceed(user_response=input_str)
                return

        raise Exception("unknown command")

    def add_expected_command(self, expected_command: ConsoleCommand):
        if not isinstance(expected_command, ConsoleCommand):
            raise Exception("Make sure you are passing a ConsoleCommand type")

        self.__expected_commands.append(expected_command)

