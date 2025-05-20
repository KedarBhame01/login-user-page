from django.shortcuts import render
import mysql.connector as sql
from django.contrib.auth.models import User
fn=''
ln=''
g=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,g,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                g=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into signup_post Values('{}','{}','{}','{}','{}')".format(fn,ln,g,em,pwd)
        # c.save()
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
