from . import jobs
from flask import render_template, redirect, session, url_for, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from ..helper import extract_date, strToInt

@jobs.route('/eligible')
@login_required
def view_jobs():
	sql1 = f"SELECT re.role_id AS role_id FROM profile AS p, roles_eligibility AS re WHERE p.stu_uid = '{session['user']['userid']}' AND re.branch = p.branch AND re.cgpa <= p.cgpa"
	role_list = db.engine.execute(sql1)
	list_of_elg_roles = []
	for each_role in role_list:
		#selecting from roles the tuples
		sql2 = f"SELECT * FROM role WHERE role_id = {each_role['role_id']}"
		res = dict(db.engine.execute(sql2).first())
		date = extract_date(str(res['last_date']))
		res['last_date'] = date
		res['status'] = 'NA'
		#to check whether already applied
		sql3 = f"SELECT status FROM application_status WHERE stu_uid = '{session['user']['userid']}' AND role_id = {each_role['role_id']}"
		flag = db.engine.execute(sql3).first()
		if flag:
			flag = dict(flag) 
			res['status'] = flag['status']
		list_of_elg_roles.append(res)
	return render_template('view_roles.html', elg_roles_list = list_of_elg_roles)


@jobs.route('/apply/<string:role_id>')
@login_required
def apply_job(role_id):
	role_id = strToInt(role_id)
	sql1 = f"INSERT INTO application_status(stu_uid, role_id, status) VALUES('{session['user']['userid']}', {role_id}, 'A')"
	db.engine.execute(sql1)
	db.session.commit()
	return redirect(url_for('jobs.view_jobs'))



