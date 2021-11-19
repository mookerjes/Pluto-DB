Introducing World's Smallest Database Engine... 'Pluto' 0.01v
Please don't expect much at this time. It's in 1% maturity state
in last 3 day's work of mine...
What To expect:
When invoked 
1) It will give you a Database Prompt named 'Pluto#:'
2) It can parse SELECT,INSERT,UPDATE,DELETE you put into the 
   command prompt named 'Pluto#:' It can only parse and format   
   and print the statements as of. 
[There is a reason why it will always print out SELECT equivalent of INSERT,UPDATE,DELETE as an output.We will transform the Constraints and Triggers by this mechanism later. One has to integrate CSVSQL and further extensions to actually get SQL query ouput]
3) In the prompt if you put 'quit' it will be out from the terminal.
Purpose of sharing: 
1) It's an Open-Source initiative and will always be.
2) So that the community can contribute and build and share and 
    grow up this database which targets to parse from any natural  
    language semantics in future.
3) Less Complexity and it will be always CSV based.
Further Work:
  1) Integrating with  
                              https://csvkit.readthedocs.io/en/latest/cli.html
  2) Processing SELECT,INSERT,UPDATE,DELETE 
                              perfectly over CSV, multiple CSV's.
  3) Processing MERGE perfectly over CSV, multiple 
                             CSV's.
  4) Implementing Constraints Logic and/or Trigger 
                             Logic perfectly over CSV, multiple CSV's.
  5) Extracting/Processing/Migrating/Loading/
                             Transforming be it OLTP or OLAP by using
   https://www.facebook.com/suman.mukherjee.5074/posts/4335609246533685
  6) Integrating with          
                                https://github.com/allenai/allennlp
Source Code:
             
Prerequisites:
             1)python 10 onwards
             2)pip3 install sqlparse [Install python and then from 
                command prompt type this]  
Invocation:
             python Pluto.py
