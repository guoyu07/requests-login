import requests


class Loginer:

    def __init__(self, login_route=None, data=None):
        """Init variables for login."""
        self._login_route = login_route if login_route else ''
        self._data = data if data else {}

    def __call__(self, baseurl, user):
        """Return login cookies."""
        url = baseurl + self._login_route
        data = dict(self._data)
        data.update(user)

        response = requests.post(url, data=data, allow_redirects=True)
        return response.cookies if self._validate(response) else None

    @staticmethod
    def _validate(response):
        """Validate if login is successful."""
        return True
