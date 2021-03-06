# Hack with Travis CI

language: cpp
# https://docs.travis-ci.com/user/multi-cpu-architectures
# https://docs.travis-ci.com/user/languages/python/#python-versions
arch:        # Removed from below: uname_result(system='Linux', node='XYZ')
  - amd64    # uname_result(release='4.15.0-1028-gcp',  version='#29~16.04.1-Ubuntu SMP', machine='x86_64',  processor='x86_64')
  - arm64    # uname_result(release='5.0.0-23-generic', version='#24~18.04.1-Ubuntu SMP', machine='aarch64', processor='aarch64')
  - aarch64  # Same as `arch: amd64`
  - ppc64le  # uname_result(release='5.0.0-23-generic', version='#24~18.04.1-Ubuntu SMP', machine='ppc64le', processor='ppc64le')
  - s390x    # uname_result(release='5.0.0-23-generic', version='#24~18.04.1-Ubuntu SMP', machine='s390x',   processor='s390x')
  - x86_64   # Same as `arch: amd64`
script:
  - uname -a
  - python3 -c "import platform ; print(platform.uname())"
  - ls -la
  - python3 --version
  - python3 -m pip || wget -qO- https://bootstrap.pypa.io/get-pip.py | sudo -H python3
  - python3 -m pip install --user flake8
  - flake8 --version
  - python3 platform_info.py
