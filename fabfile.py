from fnpdjango.deploy import *

env.project_name = 'infoscreen'
env.hosts = ['giewont.icm.edu.pl']
env.user = 'infoscreen'
env.app_path = '/srv/infoscreen'
env.services = [
    DebianGunicorn('infoscreen'),
]
