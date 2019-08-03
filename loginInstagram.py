import os
import sys
import time
import random
import requests, pickle
import json
import re

cache_dir = 'cache'
session_cache = '%s/session.txt' % (cache_dir)

instagram_url = 'https://www.instagram.com'
login_route = '%s/accounts/login/ajax/' % (instagram_url)
logout_route = '%s/accounts/logout/' % (instagram_url)
profile_route = '%s/%s/'
query_route = '%s/graphql/query/' % (instagram_url)
username = ""
password = ""
session = requests.Session()

def login():
    session.headers.update({
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.instagram.com',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'),
        'X-Instagram-AJAX': '1',
        'X-Requested-With': 'XMLHttpRequest'
    })
    session.cookies.update({
        'ig_pr': '1',
        'ig_vw': '1920',
    })

    reponse = session.get(instagram_url)
    session.headers.update({
        'X-CSRFToken': reponse.cookies['csrftoken']
    })

    time.sleep(random.randint(2, 6))

    post_data = {
        'username': username,
        'password': password
    }

    response = session.post(login_route, data=post_data, allow_redirects=True)
    response_data = json.loads(response.text)

    if 'two_factor_required' in response_data:
        identifier = response_data['two_factor_info']['two_factor_identifier']
        verification_code = input('2FA Verification Code: ')
        verification_data = {'username': username, 'verificationCode': verification_code, 'identifier': identifier}
        two_factor_response = session.post('https://www.instagram.com/accounts/login/ajax/two_factor/', data=verification_data, allow_redirects=True).json()
        if two_factor_response['authenticated']:
            session.headers.update({ 'X-CSRFToken': response.cookies['csrftoken'] })
            return two_factor_response['authenticated']
        else:
            return two_factor_response['authenticated']

    if response_data['authenticated']:
        session.headers.update({
            'X-CSRFToken': response.cookies['csrftoken']
        })

    return response_data['authenticated']


# Not so useful, it's just to simulate human actions better
def get_user_profile(username):
    response = session.get(profile_route % (instagram_url, username))
    extract = re.search(r'window._sharedData = (.+);</script>', str(response.text))
    response = json.loads(extract.group(1))
    return response['entry_data']['ProfilePage'][0]['graphql']['user']


def logout():
    post_data = {
        'csrfmiddlewaretoken': session.cookies['csrftoken']
    }

    logout = session.post(logout_route, data=post_data)

    if logout.status_code != 200:
        return False
    return True


def main(username, password):
    if not username or not password:
        sys.exit('please provide USERNAME and PASSWORD environement variables. Abording...')

    if not os.path.isdir(cache_dir):
        os.makedirs(cache_dir)

    if os.path.isfile(session_cache):
        with open(session_cache, 'rb') as f:
            session.cookies.update(pickle.load(f))
    else:
        is_logged = login()
        if is_logged == False:
            sys.exit('login failed, verify user/password combination')

        with open(session_cache, 'wb') as f:
            pickle.dump(session.cookies, f)

        time.sleep(random.randint(2, 4))

    connected_user = get_user_profile(username)
    print('You\'re now logged as {} ({} followers, {} following)'.format(connected_user['username'], connected_user['edge_followed_by']['count'], connected_user['edge_follow']['count']))

    time.sleep(random.randint(2, 4))

    
    print(' done')

if __name__ == "__main__":
    username = "lupadocidadao"
    password = "esaniagro12"
    main(username, password)