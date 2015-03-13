from distutils.core import setup
setup(
  name = 'gcmpy',
  packages = ['gcmpy'], # this must be the same as the name above
  version = '0.1',
  description = 'A python implementation of the Google Cloud Messaging server protocol for pushing messages to Android clients',
  author = 'Edward Pie',
  author_email = 'hackstockpie@gmail.com',
  url = 'https://github.com/hackstock/gcmpy', # use the URL to the github repo
  download_url = 'https://github.com/hackstock/gcmpy/tarball/0.1', # I'll explain this in a second
  keywords = ['gcm', 'gcm-server', 'push notifications'], # arbitrary keywords
  classifiers = [],
)