While True:
    try:
        answer = float(input('How many hours did you work?'))
        payrate = float(input('What is your payrate?'))
        print(f'Your total pay is ${answer*payrate:,.2f}')
        break

        #aycheck = answer*payrate
        #print(paycheck)

    except ValueError as {err}:
        pass #just passes
        #print(f'There was an error, the error is {err}.')