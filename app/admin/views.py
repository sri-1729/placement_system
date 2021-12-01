from . import admin
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from .forms import SlotForm


@admin.route('/pending_roles/', methods = ['GET', 'POST'])
@login_required
def pend_roles():
	sql = f"SELECT * FROM company WHERE admin_id IS NULL AND company_name IS NOT NULL AND company_link IS NOT NULL"
	res = db.engine.execute(sql)
	return render_template('roles_approve.html',res=res)
	
@admin.route('/allot_slots/<string:com_uid>', methods = ['GET', 'POST'])
@login_required
def allot_slots(com_uid):
	form = SlotForm()
	if form.validate_on_submit():
		i_fromdate = form.i_fromdate.data
		i_todate = form.i_todate.data
		p_fromdate = form.p_fromdate.data
		p_todate = form.p_todate.data
		t_fromdate = form.t_fromdate.data
		t_todate = form.t_todate.data
		sql = f"INSERT INTO slots(com_uid,slot_type,from_date,to_date) VALUES('{com_uid}','i','{i_fromdate}','{i_todate}')"
		res = db.engine.execute(sql)
		sql = f"INSERT INTO slots(com_uid,slot_type,from_date,to_date) VALUES('{com_uid}','p','{p_fromdate}','{p_todate}')"
		res = db.engine.execute(sql)
		sql = f"INSERT INTO slots(com_uid,slot_type,from_date,to_date) VALUES('{com_uid}','t','{t_fromdate}','{t_todate}')"
		res = db.engine.execute(sql)
		sql = f"UPDATE company set admin_id='{session['user']['userid']}' WHERE com_uid='{com_uid}' "
		ans = db.engine.execute(sql)
		return redirect(url_for('admin.pend_roles'))
	return render_template('allot_slots.html',form=form)
		
	
	
