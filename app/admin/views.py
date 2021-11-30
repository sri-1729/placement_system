from . import admin
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db


@admin.route('/pending_roles/<string:com_uid>', methods = ['GET', 'POST'])
@login_required
def pend_roles(com_uid):
	sql = f"SELECT * FROM company WHERE admin_id IS NULL AND company_name IS NOT NULL AND company_link IS NOT NULL"
	res = db.engine.execute(sql)
	if com_uid != 'NULL':
		sql = f"UPDATE company set admin_id='{session['user']['userid']}' WHERE com_uid='{com_uid}' "
		ans = db.engine.execute(sql)
		return redirect(url_for('admin.pend_roles',com_uid='NULL'))
	return render_template('roles_approve.html',res=res)
