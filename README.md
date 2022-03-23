# Official Digital License Manager library for Python

This is official python client for working with the [Digital License Manager](https://wordpress.org/plugins/digital-license-manager) API.

The library is compatible with both Python 2 and 3 and can be used in any project by installing with `pip` command.

## Installation

```
sudo pip install digital-license-manager
```

## Getting Started

To start using the Digital License Manager service you will need to host the plugin on your WordPress site. Read the [Documentation](https://docs.codeverve.com/digital-license-manager/rest-api/authentication/) for more details.

## How to use


### Initial Setup

```python
from digital_license_manager.client import Client
client = Client('http://yoursite.test', 'ck_XXXXXXXXXXXXXXXXXXXXX', 'ck_XXXXXXXXXXXXXXXXXXXXX')
```

### 1. Retrieving Licenses

```python

resp = client.find_license('AAAA-AAAA-AAAA')
if 'message' in resp:
    print('Error:' + resp.get('message'))
else:
    data = resp.get('data')
    print('License ID: ' + str(data.get('id')))
    print('License Key: ' + str(data.get('license_key')))
    print('License Expires At: ' + str(data.get('expires_at')))

```

### 2. Activating Licenses

```python

token = ''
resp = client.activate_license('AAAA-AAAA-AAAA')
if 'message' in resp:
    print('Error:' + resp.get('message'))
else:
    data = resp.get('data')
    token = data.get('token')
    license = data.get('license')
    print('Activation Token: ' + token)
    print('Activation Stats: ' + str(license.get('times_activated')) + '/' + str(license.get('activations_limit')))

```

**Note**: The token needs to be stored somewhere securely for future use (validation/deactivation/software downloads)

### 3. Validating License Activations

```python

resp = client.validate_license_activation(token)
if 'message' in resp:
    print('Error:' + resp.get('message'))
else:
    data = resp.get('data')
    license = data.get('license')
    expiresAt = (license.get('expires_at') if license else 'Never')
    deactivatedAt = (data.get('deactivated_at') if data.get('deactivated_at') else 'Never')
    print('Is Deactivated: ' + deactivatedAt)
    print('Expires At: ' + expiresAt)

```

### 4. Deactivating License Activations

```python

resp = client.deactivate_license_activation(token)
if 'message' in resp:
    print('Error:' + resp.get('message'))
else:
    data = resp.get('data')
    token = data.get('token')
    license = data.get('license')
    print('Activation Token: ' + token)
    print('Activation Stats: ' + str(license.get('times_activated')) + '/' + str(license.get('activations_limit')))

```

## Contribution

Feel free to open pull request if you noticed any bug o want to propose improvement.

## Support

If you have any questions feel free to contact us at `info@codeverve.com`

## License

```
Copyright (C) 2022 Darko Gjorgjijoski (https://codeverve.com)

This file is part of Digital License Manager

Digital License Manager Library is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

Digital License Manager Library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Digital License Manager Library. If not, see <https://www.gnu.org/licenses/>.
```