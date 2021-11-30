from . import company
from flask import render_template, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from ..helper import strToInt, formatString

@company.route('/view')
@login_required
def view_rolesProvided():
	#picking roles which company provided
	sql1 = f"SELECT role_id, title FROM role WHERE company_id = '{session['user']['userid']}'"
	roles_provided = db.engine.execute(sql1)
	list_of_roles = []
	for each_role in roles_provided:
		role = dict(each_role)
		list_of_roles.append(role)
	return render_template('view_rolesProvided.html', list_of_roles = list_of_roles)

@company.route('/students/<string:role_id>')
@login_required
def view_students_comp(role_id):
	role_id = strToInt(role_id)
	#picking students of a particular role
	sql1 = f"SELECT * FROM application_status WHERE role_id = {role_id}"
	students = db.engine.execute(sql1)
	list_of_students = []
	for each_student in students:
		student = dict(each_student)
		list_of_students.append(student)
	return render_template('view_students.html', list_of_students = list_of_students, role_id=role_id)

@company.route('/students/status/accept/<string:stu_uid>/<string:role_id>')
@login_required
def accept(stu_uid, role_id):
	stu_uid = formatString(stu_uid)
	role_id = strToInt(role_id)
	sql1 = f"UPDATE application_status SET status = 'ACC' WHERE stu_uid = '{stu_uid}' AND role_id = {role_id}"
	db.engine.execute(sql1)
	db.session.commit()
	return redirect(url_for('company.view_students_comp', role_id = role_id))

@company.route('/students/status/reject/<string:stu_uid>/<string:role_id>')
@login_required
def reject(stu_uid, role_id):
	stu_uid = formatString(stu_uid)
	role_id = strToInt(role_id)
	sql1 = f"UPDATE application_status SET status = 'REJ' WHERE stu_uid = '{stu_uid}' AND role_id = {role_id}"
	db.engine.execute(sql1)
	db.session.commit()
	return redirect(url_for('company.view_students_comp', role_id = role_id))





