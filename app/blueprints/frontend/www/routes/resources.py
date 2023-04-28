from flask import render_template, request, redirect, url_for

from app.models.resource import Resource
from app.models.resource_tag import ResourceTag
from .. import bp


@bp.route("/resources", methods=["GET", "POST"])
def resources():
    if request.form.get('search') or request.form.get('tag'):
        kwargs = {}
        if request.form.get('search'):
            kwargs['search'] = request.form.get('search')
        if request.form.get('tag'):
            kwargs['tag'] = request.form.get('tag')
        return redirect(url_for('frontend.www.resources', **kwargs, **request.args))

    if request.args.get('search'):
        resources_pages = Resource.search_by_title_pages(
            title=request.args.get('search'),
            page=int(request.args.get("page", 1)),
            per_page=9,
            tag=request.args.get('tag'),
        )
    else:
        resources_pages = Resource.all_newest_first_pages(
            page=int(request.args.get("page", 1)),
            per_page=9,
            tag=request.args.get('tag'),
        )

    tags = ResourceTag.get_all_tags()

    return render_template(
        bp.tmpl("resources.html"),
        resources=resources_pages.items,
        page=resources_pages.page,
        pages=resources_pages.pages,
        tags=tags
    )
