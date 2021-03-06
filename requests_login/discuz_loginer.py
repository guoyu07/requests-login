from requests_login.loginer import Loginer
import logging


class DiscuzLoginer(Loginer):

    def __init__(self):
        """Init varables for login."""
        login_route = '/member.php?mod=logging&action=login&loginsubmit=yes&inajax=1'
        super().__init__(login_route=login_route)

    @staticmethod
    def _validate(response):
        """Validate if login is successful."""
        logging.debug(response.text)

        if 'error' in response.text:
            return False
        return True
