# CoachingDB
Data and Applications course assignment for the management of database for Coaching Institute

1)How to run?
1. Run this on terminal "mysql -u username -p < COACHING.sql" without using quotes
								or
	Copy the contents of the COACHING.sql file and paste it in the mysql CLI.							
2. Download the coaching.py python script to your system and then run it with "python3 coaching.py".

3. Enter the username and password you have set for mysql and we're good to go!!

Note: If python library "tabulate" is not pre-installed, then install it by running the command "pip3 install tabulate"

2)Functions Available:
    
    Update funtions:-
    	1. Add
    	2. Update
    	3. Delete

    Query Functions:-

    	1. Retrieval:
    		a) View (selection)
    		b) Projection
    		c) Aggregate
    			i. Min
    			ii. Max
    			iii. Avg

    	2. Data Analysis:
    		a) Sex-Ratio
    		b) Progress

3)Suggestions while running the python script

	a. Username and password prompt at the beginning refer to the mysql username and password that
	   have the access to the database (COACHING).
	b. Since various IDs have a peculiar format, it is advised to first use view function in order 	  to be sure with inputs(Case sensitive!).
	c. To make database cleaner and easier to use, we have made few changes in the database when 	compared to the ones in the phases 1,2 & 3.
	