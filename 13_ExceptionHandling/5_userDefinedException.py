# Here we are just learning how to write used-defined error class


class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg


try:
    raise MyError("My error")

except MyError as err:
    print(err)
