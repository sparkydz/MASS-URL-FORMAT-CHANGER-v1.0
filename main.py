import sys
#MAIN FUNCTION:
def logo():
   x = """  __  __           _____ _____   _    _ _____  _        ______ ____  _____  __  __       _______    _____ _    _          _   _  _____ ______ _____  
 |  \/  |   /\    / ____/ ____| | |  | |  __ \| |      |  ____/ __ \|  __ \|  \/  |   /\|__   __|  / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \ 
 | \  / |  /  \  | (___| (___   | |  | | |__) | |      | |__ | |  | | |__) | \  / |  /  \  | |    | |    | |__| |  /  \  |  \| | |  __| |__  | |__) |
 | |\/| | / /\ \  \___ \\___ \  | |  | |  _  /| |      |  __|| |  | |  _  /| |\/| | / /\ \ | |    | |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  / 
 | |  | |/ ____ \ ____) |___) | | |__| | | \ \| |____  | |   | |__| | | \ \| |  | |/ ____ \| |    | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \ 
 |_|  |_/_/    \_\_____/_____/   \____/|_|  \_\______| |_|    \____/|_|  \_\_|  |_/_/    \_\_|     \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\v.1.0
                                                                                                                 by SparkyDz                              
                                                                                                                              
                                                                                                                      
   +------------------------+---------------------------+
   | 1)FROM WWW.SITE1.COM TO HTTP://WWW.SITE.COM (BULK) |
   | 2)FROM HTTP://WWW.SITE.COM TO WWW.SITE.COM (BULK)  |
   | 00)Exit..                                          |
   +------------------------+---------------------------+	  
        """
   print(x)
   print("Make a choice ...")
   choice=str(input())
   if choice =='1':
     www2http()
   elif choice =='2':
     http2www()
   else:
     exit(1)
def cls():
  print("\n" * 100)

def www2http():
  #input file:
  print("Write your input file : ")
  a=str(input())
  print("Write your output file : ")
  b=str(input())
  fin = open(a, "rt")
  #output file to write the result to
  fout = open(b, "wt")
  #for each line in the input file
  for line in fin:
     #read replace the string and write to output file
	   fout.write(line.replace('www.', 'http://www.'))
 #close input and output files
  fin.close()
  fout.close()
  cls()
  carry_on()
def http2www():
  #input file:
  print("Write your input file : ")
  a=str(input())
  print("Write your output file : ")
  b=str(input())
  fin = open(a, "rt")
  #output file to write the result to
  fout = open(b, "wt")
  #for each line in the input file
  for line in fin:
     #read replace the string and write to output file
	   fout.write(line.replace('http://www.', 'www.'))
 #close input and output files
  fin.close()
  fout.close()
  cls()
  carry_on()
def carry_on():
  print("Press 'Y' to continue or 'E' to exit")
  me=str(input())
  if me =='Y':
    logo()
  else:
     sys.exit(0)
#end
logo()
