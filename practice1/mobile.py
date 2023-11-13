from enum import Enum
from colorama import Fore, Style
from typing import Type


class Mobile:
    class Status(Enum):
        OFF = 0
        ON = 1

    class LogLevel(Enum):
        INFO = 0
        WARNING = 1
        ERROR = 2

    default_apps = ('Web Browser', 'Music', 'Clock', 'Email')

    def __init__(self, name: str):
        self.name = name

        self.power_off_error_occurred = False
        self.status = Mobile.Status.OFF.value
        self.apps = list(Mobile.default_apps)

    @staticmethod
    def _operation(func):
        def wrapper(self: Type['Mobile'], *args, **kwargs):
            if self.power_off_error_occurred or not self._is_operable():
                return
            func(self, *args, **kwargs)
        return wrapper

    # region Operations
    def power_on(self):
        if self.status == Mobile.Status.ON.value:
            self.log('already powered on', Mobile.LogLevel.WARNING)
            return
        self.status = Mobile.Status.ON.value
        self.power_off_error_occurred = False
        self.log('powered on')

    @_operation
    def power_off(self):
        self.status = Mobile.Status.OFF.value
        self.log('powering off...')

    @_operation
    def install_apps(self, *apps):
        for app in apps:
            if app in self.apps:
                self.log(f'app {app} already installed', Mobile.LogLevel.WARNING)
                return
            self.apps.append(app)
            self.log(f'installed app {app}')

    @_operation
    def uninstall_apps(self, *apps):
        for app in apps:
            if app in Mobile.default_apps:
                self.log(f'app {app} is a default app', Mobile.LogLevel.ERROR)
                return
            if app not in self.apps:
                self.log(f'app {app} not installed', Mobile.LogLevel.ERROR)
                return
            self.apps.remove(app)
            self.log(f'unistalled app {app}')
    # endregion

    # region Debugging
    def _is_operable(self):
        if self.status != 1:
            self.log('can\'t operate while powered off', Mobile.LogLevel.ERROR)
            self.power_off_error_occurred = True
        return self.status == 1

    def log(self, msg: str, level=LogLevel.INFO):
        colors = (Fore.GREEN, Fore.YELLOW, Fore.RED)
        print(f'{colors[level.value]}{self.name} > {msg}{Style.RESET_ALL}')
    # endregion


if __name__ == '__main__':
    mobile1 = Mobile('XYZ')
    # there will be an error because we didn't power_on the mobile first, so any operation will be ignored
    mobile1.install_apps('a', 'b', 'c')
    mobile1.uninstall_apps('b', 'c')
    print(f'installed apps in {mobile1.name}: {mobile1.apps}\n')

    mobile2 = Mobile('UVW')
    mobile2.power_on()
    mobile2.install_apps('f', 'g', 'h')
    mobile2.uninstall_apps('h')
    mobile2.power_off()

    print(f'installed apps in {mobile2.name}: {mobile2.apps}')
