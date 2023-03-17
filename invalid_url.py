# Invalid URL exception
class InvalidURL(Exception):
    def __init__(self, message="Error: Invalid Youtube URL"):
        self.message = message


if __name__ == "__main__":
    # Test the InvalidURL exception
    try:
        raise InvalidURL("This is a custom error message")
    except InvalidURL as e:
        print(e.message)
