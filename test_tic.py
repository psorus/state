from state import state

import random


class tic(state):
  
  def getstates(s):return ["new","clean","p1","p2","won","draw","finished"]
  
  def __init__(s):
    state.__init__(s,"new")
    s.clearboard()
    
  def clearboard(s):
    print("cleaning board")
    s.q=[[0,0,0],[0,0,0],[0,0,0]]
    s.winner=0
    
  
  def start(s):
    print("starting")
    assert s.iseitherstate(["new","clean"])
    if random.random()>0.5:
      s.setstate("p1")
    else:
      s.setstate("p2")
  
  def play(s,who,what):
    assert s.isstate("p"+str(who))
    assert s.q[what[0]][what[1]]==0
    print(str(who)+" is playing "+str(what))
    s.q[what[0]][what[1]]=who
    
    if not s.testwin():s.setstate("p"+str(3-who))
    
  
  def testwin(s):
    posw=[[0,1,2],
          [3,4,5],
          [6,7,8],
          [0,3,6],
          [1,4,7],
          [2,5,8],
          [0,4,8],
          [2,4,6],
          ]
    sq=[]
    for qq in s.q:
      for qqq in qq:
        sq.append(qqq)
    for p in posw:
      if sq[p[0]]!=0 and sq[p[0]]==sq[p[1]] and sq[p[1]]==sq[p[2]]:
        s.winner=sq[p[0]]
        s.setstate("won")
        return True
    p=[1 for qq in s.q if 0 in qq]
    if len(p)==0:
      s.winner=0
      s.setstate("draw")
      return True
    return False
  def init_won(s,leave):
    print(str(s.winner)+" won")
    s.setstate("finished")
  def init_draw(s,leave):
    print("draw")
    s.setstate("finished")
  
  def init_finished(s,leave):
    print("finished game, cleaning up")
    s.setstate("clean")
  
  def init_clean(s,leave):
    s.clearboard()
    # s.start()
  
  def posmoves(s):
    ret=[]
    for i in range(3):
      for j in range(3):
        if s.q[i][j]==0:ret.append([i,j])
    return ret
  
  
class tic1(tic):
  def __init__(s):
    tic.__init__(s)
    
  def init_p1(s,leave):
    
    s.play(1,random.choice(s.posmoves()))

  def init_p2(s,leave):
    
    s.play(2,random.choice(s.posmoves()))


    
if __name__=="__main__":
  x=tic1()
  for i in range(10):
    x.start()






