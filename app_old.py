from flask import Flask

from state import state

#the whole server has the same state
class fstate(state):
  def getstates(s):return ["initial","logged_in","logged_out"]
  
  def __init__(s,nam=None):
    state.__init__(s,"initial")
    if nam is None:nam=__name__
    s.app=Flask(nam)
    s.addroute()
  
  def run(s):
    s.app.run()
  
  def addroute(s):
    s.app.add_url_rule("/<k>","update",s.update)
    s.app.add_url_rule("/","main",s.main)
  
  def content(s):
    goto={"initial":"logged_in","logged_in":"logged_out","logged_out":"initial"}
    texts={"initial":"Log yourself in","logged_in":"Log yourself out","logged_out":"Go back to login"}
    return f'''<a href="\{goto[s.getstate()]}">{texts[s.getstate()]}</a>'''
  
  
  def update(s,k):
    s.setstate(str(k))
    return s.main()
  
  def main(s):
    

    
    return s.content()

x=fstate()

if __name__=="__main__":
  print("running")
  x.run()



