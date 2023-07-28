import pathlib

from flask import Flask
from kerko.composer import Composer
from flask_babel import Babel
from flask_bootstrap import Bootstrap4
from kerko import blueprint as kerko_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '*************'  # Replace this value.
app.config['KERKO_ZOTERO_API_KEY'] = '*************'  # Replace this value with API for Zotero library.
app.config['KERKO_ZOTERO_LIBRARY_ID'] = 'XXXXXXX'  # Replace this value from link to Zotero library.
app.config['KERKO_ZOTERO_LIBRARY_TYPE'] = 'group'  # Replace this value if necessary.
app.config['KERKO_DATA_DIR'] = str(pathlib.Path(__file__).parent / 'data' / 'kerko')
app.config['KERKO_COMPOSER'] = Composer()

babel = Babel(app)
bootstrap = Bootstrap4(app)

app.register_blueprint(kerko_blueprint, url_prefix='/SCSUAuthors')
