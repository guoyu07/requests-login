import requests


class Loginer:

    def __init__(self, query=None, data=None):
        """Init variables for login."""
        self._query = query if query else ''
        self._data = data if data else {}

    def __call__(self, baseurl, user):
        """Return login cookies."""
        url = baseurl + self._query
        data = dict(self._data)
        data.update(user)

        response = requests.post(url, data=data)
        return response.cookies if self._validate(response) else None

    @staticmethod
    def _validate(response):
        """Validate login is successful."""
        return True
