# command_decorator.py
command_map = {}


def command(name):
    def decorator(func):
        command_map[name] = func
        return func

    return decorator
