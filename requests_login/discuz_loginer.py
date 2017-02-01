from requests_login.loginer import Loginer


class DiscuzLoginer(Loginer):

    def __init__(self):
        """Init varables for login."""
        query = '/member.php?mod=logging&action=login&loginsubmit=yes&inajax=1'
        super().__init__(query=query)

    @staticmethod
    def _validate(response):
        if 'succeed' in response.text:
            return True
        return False
