from flask import (
    render_template,
    Blueprint,
    request)

from flask_paginate import Pagination, get_page_parameter
from app.config import PROJECTS_DIR
import os
import json

bp = Blueprint('views', __name__, url_prefix='/')
#создание списка моих проектов
projects_path = os.listdir('/'.join(['app',PROJECTS_DIR]))
projects_path = ['/'.join(['app',PROJECTS_DIR,p]) for p in projects_path]
projects = [json.load(open(p, encoding="UTF-8")) for p in projects_path]

#пагинация
def get_projects(offset=0, per_page=10):
    return projects[offset: offset + per_page]

@bp.route("/")
def hello_world():

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 2
    offset = (page - 1 )* per_page
    pagination_projects = get_projects(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=len(projects)
    , record_name='projects',css_framework='bootstrap5',alignment ='center')

    return render_template('base.html',
                            projects = pagination_projects,
                            page = page,
                            pagination=pagination)