a,b,c = 1,1,1
def g():
      b,c = 3,4
      def h():
            c= 5
            print a,b,c
      h()
g()
