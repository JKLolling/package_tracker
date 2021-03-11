from flask import Blueprint, render_template, redirect, url_for
from app.shipping_form import ShippingForm

bp = Blueprint("main", __name__, url_prefix='')


@bp.route("/")
def main():
    return "Package Tracker"


@bp.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect(url_for('.main'))
    return render_template('shipping_requests.html', form=form)
