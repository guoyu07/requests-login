# requests-login

Simple way for logging in any forums or websites based on requests

## Features

- [Discuz](http://www.discuz.net/forum.php) support

## Getting Started

- Login forums powered by Discuz

    ```python
    from requests_login.discuz_loginer import DiscuzLoginer
    cookies = DiscuzLoginer()('http://example.com', user=dict(username='username', password='password'))
    ```
    
- Customized Login

    ```python
    from requests_login.loginer import Loginer
    query = '/member.php?mod=logging&action=login&loginsubmit=yes&inajax=1'
    data = dict(loginfield='usernmae', questionid='0')
    cookies = Loginer(query, data)('http://example.com', user=dict(username='username', password='password'))
    ```

## TODO

- Add redirects support
