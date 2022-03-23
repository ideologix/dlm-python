#!/bin/bash

build_version=$1

if [ -z "$build_version" ]
  then
    echo "No version provided"
    exit
fi

if [[ "$(python3 -V)" =~ "Python 3" ]]
then
  bin_pip="pip3"
  bin_python="python3"
else
  bin_pip="pip"
  bin_python="python"
fi

sudo "$bin_pip" uninstall digital_license_manager
rm -rf dist/digital_license_manager-$build_version.tar.gz
"$bin_python" setup.py sdist
sudo "$bin_pip" install dist/digital_license_manager-$build_version.tar.gz
