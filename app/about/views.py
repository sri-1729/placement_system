from . import about
from flask import render_template, redirect, session, url_for,jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .. import db
from ..models import Login
from ..helper import strToInt

@about.route('/', methods = ['GET'])
def placement_stat():
    stat={}
    sql_query = f'SELECT COUNT(*) FROM profile'
    student_count = db.engine.execute(sql_query).first()
    stat['student_count'] = student_count[0]

    sql_query_placed = f"SELECT COUNT(*) FROM profile where placement_status='Placed'"
    placed_count = db.engine.execute(sql_query_placed).first()
    stat['placed_count'] = placed_count[0]

    sql_query_com = f"SELECT COUNT(*) FROM login where type_='company' "
    com_count = db.engine.execute(sql_query_com).first()
    stat['com_count'] = com_count[0]
    #sql_query = f'SELECT COUNT(*) FROM profile'
    #student_count = db.engine.execute(sql_query).first()
    #count = 5
    
    sql_query_com_name = f"SELECT userid FROM login where type_='company' "
    temp = db.engine.execute(sql_query_com_name)
    stat['com_name'] = [[com_name['userid']] for com_name in temp]

    for i in range(len(stat['com_name'])):
        sql_query_roles_offered = f"SELECT role_id FROM role where company_id='{stat['com_name'][i][0]}' "
        temp = db.engine.execute(sql_query_roles_offered)
        tl = [role['role_id'] for role in temp]
        
            
            

        tfl = []
            
        for j in tl:
            sql_query_role=f"SELECT title FROM role where role_id='{j}' "
            temp1 = db.engine.execute(sql_query_role).first()
            tfl.append(temp1[0])

        stat['com_name'][i] = stat['com_name'][i]  + tfl

    
    sql_query_highest = f"SELECT DISTINCT ctc FROM role"
    temp = db.engine.execute(sql_query_highest)
    l = [strToInt (sal['ctc']) for sal in temp]
    Highest = max(l)
    stat['Highest'] = Highest

    sql_query_mean_a = f"SELECT role_id,COUNT(stu_uid) FROM application_status WHERE status = 'AF' GROUP BY role_id"
    temp = db.engine.execute(sql_query_mean_a)
    temp1 = []
    for i in temp:
        temp1.append([i['role_id'],i['count']])
    sc = 0
    sp = 0
    for i in temp1:
        sql_query_mean_b = f"SELECT ctc FROM role WHERE role_id = {i[0]} "
        temp2 = db.engine.execute(sql_query_mean_b).first()
        i.append(strToInt(temp2[0]))
        sc += i[1]
        sp += i[1] * i[2]

    if sc == 0:
        stat['mean'] = 0
    else:
        stat['mean'] = sp // sc
    

    return render_template('about.html',stat = stat)
