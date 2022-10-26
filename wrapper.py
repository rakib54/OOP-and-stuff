def do_work(work):
  print("Starting work")
  work()
  print("End work")

def work():
  print("I am from inside")

do_work(work)