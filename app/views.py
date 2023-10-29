from flask import (
    render_template,
    Blueprint)


bp = Blueprint('views', __name__, url_prefix='/')

@bp.route("/")
def hello_world():
    return render_template('index.html')