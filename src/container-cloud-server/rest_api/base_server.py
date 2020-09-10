from decorator import decorator
from quart import Quart


app = Quart(__name___)


def endpoint(version: str):
    def _wrap_func(func):
        return app.route(f'/api/{version}/{func.__name__}')(func)
