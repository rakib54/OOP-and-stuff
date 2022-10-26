def do_work():
  print("I am doing work")
  def func():
    print("I am from inside")
  return func

do_work()()