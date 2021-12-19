import sqlparse
import traceback
import sys
import cursor
import re
# Split a string containing two SQL statements:
#raw = 'select * from   DUAL   WHERE 1=3; select * from bar;'
class Custom_dot_error(Exception):
    pass
    
class Other_error(Exception):
    pass
    
raw="" 
while (raw.lower().replace(" ","").replace("\n","") != 'quit;' ):
  try:
    y = "" 
    rw = ""
    print(y)
    esc = chr(27)
    #print(f'a{esc}[5m_\u2592b\u2588{esc}[m_c')
    cursor.show()
    raw = input("Pluto#:")
    o=2
    while(';' not in raw.upper() and '...' not in raw.upper()):
        cursor.show()
        raw = raw+" "+input(str(o)+'#:')+"\n"
        #print("raw#"+raw+"#")
        cursor.show()
        o=o+1
    #print("raw->"+raw.lower()+"<-raw")
    if ('...' in raw.upper()):
       raise Custom_dot_error
    
    if ("quit;" == raw.lower().replace(" ","").replace("\n","")):
       #exit
       raise Other_error
    try:
        statements = sqlparse.split(raw)
        #print(statements)

        # Format the first statement and print it out:
        first = statements[0]
        #print(sqlparse.format(first, reindent=True, keyword_case='upper'))

        # Parsing a SQL statement:
        parsed = sqlparse.parse(first)[0]
        lst = list(parsed.tokens)
        #print(parsed.tokens)
        
        #print(parsed.tokens[-2])

        j=0  
        z=" "
        x=""        
        for i in lst:
            x = str(lst[j]).upper()
            #print(x)
            j=j+1
            if (x == 'FROM' or (z == 'FROM' and x != ' ')):
               z=x
               if (x != 'FROM'): 
                  print(str(i).upper())
                  break

        j=0 
        print(y)
        if y == "":
            for i in lst:
                x = str(lst[j]).upper()
                #print(x)
                j=j+1
                if (x == 'SELECT' and ('INSERT' not in  str(first).upper()) and ('DELETE' not in  str(first).upper()) and ('UPDATE' not in  str(first).upper())):
                   y=x
                   print("Here in " + y)
                   y = "Here in " + y
            k = 0
            while k < len(lst):
                if ('SELECT' in  str(parsed.tokens[k]).upper() and ('INSERT' not in  str(first).upper()) and ('DELETE' not in  str(first).upper()) and ('UPDATE' not in  str(first).upper())):
                   if y is not None:
                       y=y.replace("Here in ","")     
                       print("y"+y)
                   if  'WHERE' in  str(parsed.tokens[k]).upper():
                       y=None
                   second=first.upper().replace(y,"",1)
                   second=second.upper().replace(";","")
                   print("SELECT * FROM("+"SELECT "+second+")")
                   print("SELECT COUNT(*) FROM("+"SELECT "+second+")")
                   break
                k = k + 1       

        j=0  
        m="" 
        x=""
        if y == "": 
            for i in lst:
                x = str(lst[j]).upper()
                #print(x)
                j=j+1
                print("y3"+y+"y3")
                if (x == 'INSERT' or 'INSERT' in  y):                   
                   y=y + x
                   print("Here in " + y)
                   if ('INTO' in  y and x != 'INTO' and x != ' '):
                       z=x
                       break 
            
            k = 0
            while k < len(lst):       
                if ('VALUES' in  str(parsed.tokens[k]).upper()):
                    m = str(parsed.tokens[k]).upper().replace("VALUES","").replace("(","").replace(")","")   
                    print("SELECT "+m+" FROM "+z)
                    print("SELECT COUNT(*) FROM("+"SELECT "+m+" FROM "+z+")")    

                if ('SELECT' in  str(parsed.tokens[k]).upper() and 'INSERT' in  y):
                    y=y.replace("Here in ","")  
                    print("y2"+y)
                    second=first.upper().replace(y,"")
                    second=second.upper().replace(";","")
                    print("SELECT * FROM("+second+")") 
                    print("SELECT COUNT(*) FROM("+second+")")
                    break
                    
                k = k + 1    
        
        j=0 
        x=""
        if y == "": 
            for i in lst:
                x = str(lst[j]).upper()
                print(x)
                j=j+1
                if (x == 'DELETE' ):
                   y=x
                   print("Here in " + y)
                   y = "Here in " + y
                   break 
            if ('DELETE' in  first.upper() and y != ""):       
                second=first.upper().replace("DELETE FROM","SELECT * FROM ",1).replace("DELETE","SELECT * FROM ",1)
                second=second.upper().replace(";","")
                print("SELECT * FROM("+second+")") 
                print("SELECT COUNT(*) FROM("+second+")")        
                                   
        j=0 
        x=""
        if y == "": 
            for i in lst:
                x = str(lst[j]).upper()
                print(x)
                j=j+1
                if (x == 'UPDATE' ):
                   y=x
                   print("Here in " + y)
                   y = "Here in " + y
                   break 
            j=0  
            z=" "
            x=""  
            z1 = ""            
            for i in lst:
                x = str(lst[j]).upper()
                #print(x)
                j=j+1
                if (x == 'UPDATE' or (z == 'UPDATE' and x != ' ')):
                   z=x
                   if (x != 'UPDATE' and x != 'SET'): 
                      print(str(i).upper())
                      z=x
                      break       
            if ('UPDATE' in  first.upper() and y != ""): 
                k = 0
                while k < len(lst):       
                    if ('SET' in  str(parsed.tokens[k]).upper()):
                        parsed.tokens[k] = str(parsed.tokens[k]).upper()
                        j=0
                        for i in lst:
                             x = str(lst[j]).upper()
                             
                             j=j+1
                             if (x == 'SET' or (z1 == 'SET' and x != ' ')):
                                z1=x
                                if (x != 'SET'): 
                                  print(str(i).upper())
                                  z1=x
                                  z9=x
                                  print("z1"+z1)
                                  break 
                        m = str(parsed.tokens[k]).upper()
                        print(m)
                    k = k + 1
                
                g=0                
                z2 = z1.split(',')
                z4 = ""
                z5 = ""
                for q in z2:
                    f=0
                    z3=str(z2[g]).strip(" ").upper()
                    print("z3"+z3)
                    print("z3.count="+str(z3.count('=')))
                    if 'SELECT' in z3.upper()  and z3.count('=') > 1:
                       z3.upper().replace('=','##6##')
                       z3.upper().replace('##6##','=',1)
                       print(z3) 
                    r=z3.split('=')
                    while f < len(r):
                        z4=z4+r[f]+',' 
                        z5=z5+r[f+1]+','
                        break
                    g=g+1
                    
                if z4.upper() in 'SELECT' and z4.count('##6##') > 1:
                    z4.upper().replace('##6##','=')
                       
                if z5.upper() in 'SELECT' and z5.count('##6##') > 1:   
                    z5.upper().replace('##6##','=')
                       #re.sub(r'(?is)</html>.+', '</html>', article)
                first=first.replace("\n"," ")   
                second=first.upper().replace("UPDATE","SELECT * FROM (").replace(z,"",1).replace("SET "+z9,"SELECT "+z4.rstrip(',')+" FROM "+z)
                #second=first.upper().replace("UPDATE","SELECT * FROM (").replace(z,"",1).sub(r'(?SET)'+z9,"SELECT "+z4.rstrip(',')+" FROM "+z)
                second=second.upper().replace(";",")")
                third=first.upper().replace("UPDATE","SELECT * FROM (").replace(z,"",1).replace("SET "+z9,"SELECT "+z5.rstrip(',')+" FROM "+z)
                #third=first.upper().replace("UPDATE","SELECT * FROM (").replace(z,"",1).sub(r'(?SET)'+z9,"SELECT "+z5.rstrip(',')+" FROM "+z)
                third=third.upper().replace(";",")")
                print("SELECT * FROM("+second+")") 
                print("SELECT COUNT(*) FROM("+second+")") 
                print("SELECT * FROM("+third+")") 
                print("SELECT COUNT(*) FROM("+third+")")
    except Custom_dot_error as Error:     
      raise Custom_dot_error
    except Other_error as Error2:
      raise Other_error
  except Custom_dot_error as e:     
      pass
  except Other_error as e2:
      pass    
  except:
    print(sys.exc_info())
    print(traceback.print_exception)
    raw="quit;"
    raise    
           