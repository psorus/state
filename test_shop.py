from state import state


class item(state):

  def __init__(s,count=10):
    state.__init__(s,"full")
    s["count"]=count

  def getstates(s):return ["full","available","selling","sold","soldout","restocking"]
  
  def leave_soldout(s,into):return s["count"]>0 or into=="restocking"
  
  def into_selling(s,leave):return s["count"]>0
  
  def init_selling(s,leave):
    print("selling one object")
    s["count"]-=1
    s.setstate("sold")
  
  def init_sold(s,leave):
    print("gratulations")
    if s["count"]==0:
      s.setstate("soldout")
    else:
      s.setstate("available")
  
  
  def init_soldout(s,leave):
    print("out of order")
 
  
  def buy(s):
    print("trying to buy")
    s.map({"available":"selling","full":"selling","soldout":lambda:print("sadly no longer available")})
  
  def restock(s):
    print("restocking...")
    s.map({"available":"restocking","soldout":"restocking","full":lambda:print("cannot restock, already full")})
    # s.setstate("restocking")
  
  def init_restocking(s,leave):
    s["count"]+=1
    print("restocked")
    s.setstate("available")
    s.setstate("full")
  
  def into_full(s,leave):return s["count"]==10
  
  def into_restocking(s,leave):return leave != "full"
  
  def init_full(s,leave):print("completely full again")
  
  
  def available(s):
    return s.iseitherstate(["available","full"])