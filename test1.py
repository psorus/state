
class t:
  def __setitem__(s,a,v):
    print("setting item",a,v)
    return 1


tt=t()

k=(tt["a"]=1)

