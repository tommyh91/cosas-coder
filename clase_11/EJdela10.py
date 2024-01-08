def conversion(*args):
    if len(args) == 1:
        mili = args[0]
        metros = mili//1000
        mili -= metros*1000
        centi = mili//10
        mili -= centi*10
        print("la cantidad de metros es: ", metros, "la cantidad de centimetros es: ", centi, "la cantidad de mili es: ", mili)
    elif len(args) == 3:
        m = args[0]
        cm = args[1]
        mm = args[2]
        res_total = m*1000+cm*10+mm
        print("la cantidad de mm es: ", res_total)
    else:
        print("solo puede poner un argumento o 3")

conversion(4,31,3,2)