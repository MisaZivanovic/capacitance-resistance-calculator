val1 = input('Please choose what do you want to calculate, resistance or capacitance: ')
if val1 == 'resistance':
    val = input('Please choose which kind of calculation do you want to do, in paralel, or in series: ')
    if val == 'in paralel':
        def resistor_calculator(r1,r2):
            in_paralel= (r1*r2)/(r1+r2)
            return in_paralel

        r1=float(input('Please enter the value of the first resistor, in kilo ohms: '))
        r2=float(input('Please enter the value of the second resistor, in kilo ohms: '))

        print('For the first resistor value, you have entered',r1,'kilo ohms and for the second resistor value you have entered',\
        r2,'kilo ohms the result of this calculation is',resistor_calculator(r1,r2),' kilo ohms. Thank you for using our calculator.')
    if val == 'in series':
        def resist_ser(r1, r2):
            series = r1+r2
            return series

        r1=float(input('Please enter the value of the first resistor, in kilo ohms: '))

        r2=float(input('Please enter the value of the second resistor, in kilo ohms: '))

        print('For the first resistor value, you have entered',r1,'kilo ohms and for the second resistor value you have entered',\
        r2,'kilo ohms the result of this calculation is',resist_ser(r1, r2),' kilo ohms.\
         Thank you for using our calculator.')
if val1 == 'capacitance':
    val2 = input('Please choose which kind of calculation do you want to do, in paralel, or in series: ')
    if val2=='in paralel':
        def cap_par(c1,c2):
            cparalel = c1+c2
            return cparalel

        c1=float(input('Please enter capacitor 1 value in microFarads (uF): '))
        c2=float(input('Please enter capacitor 2 value in microFarads (uF): '))

        print('C1 one value is',c1,'uF and C2 value is', c2,'uf. The result of the chosen calculation is',cap_par(c1,c2),'uF. Thank you for using our calculator.')
    if val2 == 'in series':
        def cap_ser(c1,c2):
            cseries = 1/(1/c1+1/c2)
            return cseries

        c1=float(input('Please enter capacitor 1 value in microFarads (uF): '))
        c2=float(input('Please enter capacitor 2 value in microFarads (uF): '))

        print('C1 one value is',c1,'uF and C2 value is', c2,'uf. The result of the chosen calculation is',cap_ser(c1,c2),'uF. Thank you for using our calculator.')
