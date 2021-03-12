from flask import Blueprint, render_template, redirect, url_for
from app.shipping_form import ShippingForm
from app.models import Package, db

bp = Blueprint("main", __name__, url_prefix='')


@bp.route("/")
def main():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@bp.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(
            sender=data['sender'],
            recipient=data['recipient'],
            origin=data['origin'],
            destination=data['destination'],
            location=data['origin']
        )
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect(url_for('.main'))
    return render_template('shipping_requests.html', form=form)
