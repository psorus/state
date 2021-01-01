from flask import Flask,make_response,request

from state import state

import random



class fstate(state):
  def getstates(s):return ["initial","logged_in","logged_out"]
  
  def __init__(s):
    state.__init__(s,"initial")


  
 
  
  def content(s):
    goto={"initial":"logged_in","logged_in":"logged_out","logged_out":"initial"}
    texts={"initial":"Log yourself in","logged_in":"Log yourself out","logged_out":"Go back to login"}
    return f'''<a href="\{goto[s.getstate()]}">{texts[s.getstate()]}</a>'''
  
  
  def update(s,k):
    s.setstate(str(k))
    return s.main()
  
  def main(s):
    

    
    return s.content()

class controller():
  def __init__(s,nam=None):
    s.q={}
    if nam is None:nam=__name__
    s.app=Flask(nam)
    s.addroute()
   
  def addroute(s):
    s.app.add_url_rule("/<k>","update",s.update)
    s.app.add_url_rule("/","main",s.main)
  def run(s):
    s.app.run()
    
  def genuid(s):
    return int(1000+random.random()*8999.9)

  def createnew(s,uid):
    s.q[uid]=fstate()
  def findwho(s):
    resp=[]
    uid = request.cookies.get('uid')
    if uid is None:
      print("!!!no cookie yet")
    if not uid in s.q:
      print("!!!uid not known")
    if (uid is None) or (not uid in s.q):
      uid=s.genuid()
      s.createnew(uid)
      resp.append(["uid",str(uid)])
    print("keys",s.q.keys(),"uid",uid)
    return s.q[uid],resp
  
  def call(s,what,*param):
    obj,resp=s.findwho()
    assert hasattr(obj,what)
    q=getattr(obj,what)(*param)
    # print("returning",q)
    ret=make_response(q)
    for r in resp:
      ret.set_cookie(*r)
    # print("made response")
    return ret
  
  def update(s,k):
    return s.call("update",k)
    return s.main()
    # return str(session["uid"])+"\n"+s.findwho().update(k)
  
  def main(s):
    return s.call("main")
    ret="Hello World"
    ret+="\n"
    ret+=s.findwho()
    return ret
    resp=make_response(ret)
    # resp.set_cookie("test1","I am the cookie")
    return resp
    return str(session["uid"])+"\n"+s.findwho().main()



x=controller()


if __name__=="__main__":
  print("running")
  x.run()



