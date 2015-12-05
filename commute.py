#Find out how much your commutes will cost, and how many extra oil changes you will need.

print "This program will estimate how much your commute will cost over the course of a year."

def commutes():
    # Tries these inputs against the except value. Need to TRY against the variables instead of input, should solve unbound exception
    try:
        print "Please enter the estimated price of gas."
        gas_price = float(raw_input("> "))#accepts float for input instead of string or int

        print "How many gallons of gas can your tank hold?"
        tank_size = float(raw_input("> "))

        print "What is your estimated gas mileage?"
        miles_per_gallon = float(raw_input("> "))

        print "How many miles from starting point to destination?"
        global miles #Makes miles a global variable instead of a local.  Fixes an unbound error that sometimes displays.  Unbound error occurs because variables set inside TRY code block instead of before.
        miles = float(raw_input("> "))

        print "How many days a week will you make this trip?"
        days_worked = float(raw_input("> "))
    # Creates an exception for the error when input is null or 0. Restarts function.  Figure out how to ask same question and continue with function rather than restart. ZeroDiv is not working, as written or as a seperate exception.  EXCEPT may be the wrong way to go about this.  Maybe IF or WHILE instead.
    except (ValueError, ZeroDivisionError): 
        print "---> Please try again.  Must be a number and must be greater than 0. <---\n"
        commutes()       
    

    #miles
    total_miles = miles * 2 
    miles_week = total_miles * days_worked
    miles_month = miles_week * 4
    miles_year = miles_month * 12 

    #gas
    daily_gas = total_miles / miles_per_gallon
    gas_week = daily_gas * days_worked
    fillup = gas_week / tank_size
    fillup_month = fillup * 4
    cost_week = gas_week * gas_price
    cost_month = cost_week * 4
    cost_year = cost_month * 12

    #oil
    oil = 3000.00
    oil_month = oil - miles_month
    extra_oil = miles_year / oil 

    # %0.2f is the placeholder for floating point.  0.2 mean that it will show two decimal places, rounded up.
    
    #Change to a simpler output to be more concise and easier to read. Perhaps add for tire rotations and tire replacement.
    #Output miles
    print "Miles driven per day: %0.2f" % total_miles
    print "Miles driven per week: %0.2f" % miles_week
    print "Miles driven per month: %0.2f" % miles_month
    print "Miles driven a year: %0.2f" % miles_year

    #Output gas
    print "Gallons used per day: %0.2f" % daily_gas
    print "Gallons used per week: %0.2f" % gas_week
    if fillup >= 1:
        print "You will have to refill your tank %d time(s) per week." % fillup
        print "You will have to refill your tank %d time(s) per month." % fillup_month
    else:
        print "This commute uses less than a tank per week."
        print "You will have to refill your tank %d time(s) per month." % fillup_month
    print "It will cost $%0.2f a week for gas." % cost_week
    print "It will cost $%0.2f a month for gas." % cost_month
    print "It will cost $%0.2f a year for gas." % cost_year

    #Output oil
    if oil_month > 1 and extra_oil > 1:
        print "%0.2f miles left each month until oil change at 3,000 miles" % oil_month
        print "You will have %d extra oil changes a year." % extra_oil
    elif oil_month > 1 and extra_oil < 1:
        print "%0.2F miles left each month until oil change at 3,000 miles." % oil_month
    else:
        print "You will have %d extra oil changes a year." % extra_oil
commutes()
