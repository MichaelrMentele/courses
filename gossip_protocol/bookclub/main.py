import sys

from flask import Flask
from views.views import UpdateFavoriteView, MemberAPI

from helpers.helpers import RedisWrapper, favorite_picker_task

###############
# Handle Args #
###############
try:
    name = sys.argv[1]
except IndexError:
    name = 'roger'

try:
    db = sys.argv[2]
except IndexError:
    db = 0

try:
    port = sys.argv[3]
except IndexError:
    port = 5000

#########
# Setup #
#########
app = Flask(name)
app.config['redis_db'] = int(db)
app.config['port'] = int(port)
redis = RedisWrapper(db=app.config['redis_db'])

##########
# Routes #
##########
app.add_url_rule(
    '/update_favorite',
    view_func=UpdateFavoriteView.as_view('update_favorite'),
    port=app.config['port'],
    redis=redis
)

member_api = MemberAPI.as_view('member_api')
app.add_url_rule(
    '/members/',
    defaults={'member_port': None},
    view_func=member_api,
    methods=['GET']
)
app.add_url_rule(
    '/members/',
    view_func=member_api,
    methods=['POST']
)

#######
# Run #
#######
if __name__ == "__main__":
    favorite_picker_task(port)
    app.run(port=app.config['port'])
