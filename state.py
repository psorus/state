from abc import ABCMeta,abstractmethod


class state:
  """Each class supports a leave(leave,into)->bool, with which you can stop the transformation from leave into into (return False to stop the execution).
Also there is the less general leave_[state0](into)->bool, which is called after the general one.
After those two, the very similar into(leave,into)->bool and into_[state](leave)->bool functions are called, again beeing able to chance the reparametrisation.
Finally when none of the previous functions was defined and returned False, init(leave,into) and init_[state](into) are called after the state is updated

I suggest not calling any elements like your state, since this can have unseen consequences

Instead of setting each of the function to be a function, you can also utilize dictionary[param], a constant or a list, which will be interpreted as stop if either stops. If you set it to a string it will set the state to this instead

each state implements also state variables, which are accessed by brackets.
Accessing any state variable calls returns values modified by vision_[variable](value)->value and vision(variable,value)->value and functions of names like call_[variable](value) and call(variable,value) are simply called. Trying to write any variable calls functions first to transform (trafo_[variable](old_value,new_value)->value and trafo(variable,old_value,new_value)->value) and then, using the transformation result shallwrite_[variable](old_value,new_value)->bool and shallwrite(variable,old_value,new_value)->bool, which can stop the overwriting of a variable by returning False, and after successfully overwriting any variable, write_[variable](old_value,new_value) (and write(variable,old_value,new_value)) is called.

  
  """
  
  @abstractmethod
  def getstates(s) -> "[str]":
    """method to return the number of states currently possible, can be state dependent, but will be called a lot"""
    pass
  
  def _getstate(s,s0):
    states=s.getstates()
    if not s0 in states:
      try:
        s0=states[int(s0)]
      except:
        raise Exception("The state "+str(s0)+" is not valid\nValid states are\n"+"\n".join(states))
    return s0
  
  def __init__(s,s0=0):
    s.state=s._getstate(s0)
    s.q={}
  
  def _processreturn(s,q,param):
    """if False, stop execution"""
    if not type(param) is list:param=[param]
    if callable(q):
      return q(*param)
    elif type(q) is dict:
      return s._processreturn(q[param[0]],param[1:])
    elif type(q) is list:
      ret=True
      for qq in q:
        ret=ret and s._processreturn(qq,param)
      return ret
    elif type(q) is str:
      s.setstate(q)
      return False
    else:
      return q
  def setstate(s,state=0) -> "successful value set":
    s0=str(s.getstate())
    v1=s._getstate(state)
    s1=str(v1)
    if hasattr(s,"leave_"+s0):
      if not s._processreturn(getattr(s,"leave_"+s0),s1):return False

    if hasattr(s,"leave"):
      if not s._processreturn(getattr(s,"leave"),[s0,s1]):return False
    
    if hasattr(s,"into_"+s1):
      if not s._processreturn(getattr(s,"into_"+s1),s0):return False
    if hasattr(s,"into"):
      if not s._processreturn(getattr(s,"into"),[s0,s1]):return False
    
    s.state=v1
    
    if hasattr(s,"init_"+s1):
      getattr(s,"init_"+s1)(s0)
    if hasattr(s,"init"):
      getattr(s,"init")(s0,s1)

    return True

  def _assertinit(s):
    if not hasattr(s,"state"):raise Exception("the state has not been initialised. Call state.__init__(s,s0) at the beginning of your class initialiser first\nThe Error occured at\n"+str(s))

  def getstate(s) -> "str":
    s._assertinit()
    return s.state

  def isstate(s,s0) ->"bool":
    s._assertinit()
    s0=s._getstate(s0)
    return s0==s.state
  
  def iseitherstate(s,s0) ->"bool":
    for q in s0:
      if s.isstate(q):return True
    return False
  
  def map(s,dic):
    """function to do stuff according to a dictionary of the current state. I suggest the dictionary keys to include all possible states. Values can be either new states or callable objects. Returns either the output of the function, or the return of s.setstate"""
    state=s.getstate()
    if not state in dic:raise Exception("the current state "+str(state)+" is not available to map to using the dictionary "+str(dic))
    val=dic[state]
    if callable(val):
      return val()
    states=s.getstates()
    if val in states:
      return s.setstate(val)
    raise Exception("I dont know how to use this "+str(state)+" since it maps to a type of "+str(type(val))+" namely "+str(val))
  
  def cycle(s):
    d=s.getstates()
    ld=len(d)
    return s.map({d[i]:d[(i+1)%ld] for i in range(ld)})
  
  def __getitem__(s,a):
    if not a in s.q.keys():raise Exception("state variable "+str(a)+" is not defined")
    
    s0=str(a)
    v=s.q[a]

    if hasattr(s,"vision_"+s0):
      v=getattr(s,"vision_"+s0)(v)
    if hasattr(s,"vision"):
      v=getattr(s,"vision")(s0,v)

    if hasattr(s,"call_"+s0):
      getattr(s,"call_"+s0)(v)
    if hasattr(s,"call"):
      getattr(s,"call")(s0,v)


    return v
    
    
  def __setitem__(s,a,v):#maybe also introduce "delete variable" "create variable"
    old=None
    if a in s.q.keys():old=s.q[a]
    
    s0=str(a)

    if hasattr(s,"trafo_"+s0):
      v=getattr(s,"trafo_"+s0)(old,v)
    if hasattr(s,"trafo"):
      v=getattr(s,"trafo")(s0,old,v)


    if hasattr(s,"shallwrite_"+s0):
      if not s._processreturn(getattr(s,"shallwrite_"+s0),old,v):return False

    if hasattr(s,"shallwrite"):
      if not s._processreturn(getattr(s,"shallwrite"),[s0,old,v]):return False
    
    
    
    s.q[a]=v
  
    if hasattr(s,"write_"+s0):
      getattr(s,"write_"+s0)(old,v)
    if hasattr(s,"write"):
      getattr(s,"write")(s0,old,v)

    


