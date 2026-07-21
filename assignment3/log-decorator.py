import logging
import functools

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        positional = list(args) if args else "none"
        keyword = kwargs if kwargs else "none"
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {positional}")
        logger.log(logging.INFO, f"keyword parameters: {keyword}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def takes_positional(*args):
    return True


@logger_decorator
def takes_keyword(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    takes_positional(1, 2, 3)
    takes_keyword(a=1, b=2)