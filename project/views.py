from apistar import http
from datetime import datetime


def timestamp(time):

    def from_natural(time):
        unix = int(datetime.strptime(time, "%B %d, %Y").timestamp())
        return {"unix": unix, "natural": time}

    def from_unix(time):
        unix = int(time)
        natural = datetime.fromtimestamp(unix).strftime("%B %d, %Y")
        return {"unix": unix, "natural": natural}

    for f in [from_natural, from_unix]:
        try:
            return f(time)
        except ValueError:
            continue

    return {"unix": None, "natural": None}
