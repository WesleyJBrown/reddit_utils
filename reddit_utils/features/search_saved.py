
from flask import (
    Blueprint, render_template
)

from ..auth import api_access_required
from .search_common import search_page

bp = Blueprint('search_saved', __name__)



@bp.route('/search/saved', methods=('GET', 'POST'))
@api_access_required
def main():
    search_results = search_page()
    return render_template('features/search_saved.htm.j2', search_results=search_results)
