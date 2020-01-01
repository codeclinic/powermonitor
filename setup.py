from distutils.core import setup
setup(
  name = 'TuyaPowerStats',         # How you named your package folder (MyLib)
  packages = ['TuyaPowerStats'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Reports all the power stats from a Tuya socket or switch including newer v3.3 protocol devices',   # Give a short description about your library
  author = 'Phill Healey,                   # Type in your name
  author_email = 'phill@codeclinic.de',      # Type in your E-Mail
  url = 'https://github.com/codeclinic/TuyaPowerStats',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/codeclinic/TuyaPowerStats/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TUYA', 'POWER', 'STATS', 'DATA', 'REPORTING', 'SWITCH', 'SOCKET', 'OUTLET', 'SMARTLIFE', 'JINVOO'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pycrypto',
          'pycryptodome',
          'paes',
          'pytuya',
          'paho-mqtt',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)