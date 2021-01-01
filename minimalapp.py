from flask import Flask,make_response

from state import state


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
    

  def update(s,k):
    return s.main()

  
  def main(s):
    ret="Hello World"
    # return ret
    resp=make_response(ret)
    resp.set_cookie("test1","I am the cookie")
    return resp
    # return str(session["uid"])+"\n"+s.findwho().main()



x=controller()


if __name__=="__main__":
  print("running")
  x.run()



