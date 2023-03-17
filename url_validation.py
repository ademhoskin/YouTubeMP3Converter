# re for url validation, uses Invalid URL
import re
from invalid_url import InvalidURL


def validate_url(url):
    # regex validation/exception implementation
    url_pattern = re.compile(r'https?://(www\.)?youtube\.com/watch\?v=\w+')
    if url_pattern.match(url):
        return True
    else:
        raise InvalidURL()


if __name__ == "__main__":
    print('Running URL validation script')
