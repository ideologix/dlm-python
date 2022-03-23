from json import dumps
from pprint import pprint

from digital_license_manager.client import Client

client = Client('http://dlm.test', 'ck_77633b1c12b56efc951856e645c65dd70dddd111', 'cs_b9991a061c43b8b8681714498f5b80c2e002c020')

license_key = 'W0Z2-5203-CCA1-Z055'

# Usage of find_license()
resp = client.find_license(license_key)
if 'code' not in resp:
    data = resp.get('data')
    print('License ID: ' + str(data.get('id')))
    print('License Key: ' + str(data.get('license_key')))
    print('License Expires At: ' + str(data.get('expires_at')))
else:
    print(resp.get('message'))

# Usage of activate_license()
token = ''
resp = client.activate_license(license_key)
if 'code' not in resp:
    data = resp.get('data')
    token = data.get('token')
    license = data.get('license')
    print('Activation Token: ' + token)
    print('Activation Stats: ' + str(license.get('times_activated')) + '/' + str(license.get('activations_limit')))
else:
    print(resp.get('message'))

# Usage of validate_license_activation()
resp = client.validate_license_activation(token)
if 'code' not in resp:
    data = resp.get('data')
    license = data.get('license')
    expiresAt = (license.get('expires_at') if license else 'Never')
    deactivatedAt = (data.get('deactivated_at') if data.get('deactivated_at') else 'Never')
    print('Is Deactivated: ' + deactivatedAt)
    print('Expires At: ' + expiresAt)
else:
    print(resp.get('message'))

# Usage of deactivate_license_activation()
resp = client.deactivate_license_activation(token)
if 'code' not in resp:
    data = resp.get('data')
    license = data.get('license')
    print('Deactivation Token: ' + token)
    print('Activation Stats: ' + str(license.get('times_activated')) + '/' + str(license.get('activations_limit')))
else:
    print(resp.get('message'))

# Usage of validate_license_activation()
resp = client.validate_license_activation(token)
if 'code' not in resp:
    data = resp.get('data')
    license = data.get('license')
    expiresAt = (license.get('expires_at') if license else 'Never')
    deactivatedAt = (data.get('deactivated_at') if data.get('deactivated_at') else 'Never')
    print('Is Deactivated: ' + deactivatedAt)
    print('Expires At: ' + expiresAt)
else:
    print(resp.get('message'))
