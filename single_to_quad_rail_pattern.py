def gen_sr_qr(word, rail, wr_il_script):

    bitn1, bitn = word[::2], word[1::2]

    b = len(bitn)
    c = len(word)

    drt = [0] * c
    drf = [0] * c
    ndrt = [0] * c
    ndrf = [0] * c

    z = b - 1
    y = (b + b) - 1

    while z >= 0:
        if bitn[z] == 0:
            drt[y] = 0
            ndrt[y] = 1
            drf[y] = 1
            ndrf[y] = 0
        elif bitn[z] == 1:
            drt[y] = 1
            ndrt[y] = 0
            drf[y] = 0
            ndrf[y] = 1

        drt[y-1] = 0
        ndrt[y-1] = 1
        drf[y-1] = 0
        ndrf[y-1] = 1
        z = z - 1
        y = y - 2

    if wr_il_script == 1:
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vL0", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*drt, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vL1", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*drt, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNL0", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*ndrt, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNL1", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*ndrf, sep="", end='')
        print("\")")
    elif wr_il_script == 2:
        print("if(schObjPropForm->instanceName->value == \"vL0", end = '')
        print(rail, end = '')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end = '')
        print(*drt, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vL1", end='')
        print(rail, end='')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*drf, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNL0", end='')
        print(rail, end='')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*ndrt, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNL1", end='')
        print(rail, end='')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*ndrf, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")
    else:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Generate rails for rail-", rail)
        print("Single rail complete:", word)
        print("Single rail bit    n:", bitn)
        print("Single rail bit  n-1:", bitn1)
        print("----------------------------------")
        print("For bitn:")
        print("Quad-rail normal true:  L0", rail)
        print(*drt, sep="")
        print("Quad-rail normal true:  L1", rail)
        print(*drf, sep="")
        print("Quad-rail invert true: NL0", rail)
        print(*ndrt, sep="")
        print("Quad-rail invert true: NL1", rail)
        print(*ndrf, sep="")

    b = len(bitn1)

    drt = [0] * c
    drf = [0] * c
    ndrt = [0] * c
    ndrf = [0] * c

    z = b - 1
    y = (b + b) - 1

    while z >= 0:
        if bitn1[z] == 0:
            drt[y] = 0
            ndrt[y] = 1
            drf[y] = 1
            ndrf[y] = 0
        elif bitn1[z] == 1:
            drt[y] = 1
            ndrt[y] = 0
            drf[y] = 0
            ndrf[y] = 1

        drt[y - 1] = 0
        ndrt[y - 1] = 1
        drf[y - 1] = 0
        ndrf[y - 1] = 1
        z = z - 1
        y = y - 2

    if wr_il_script == 1:
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vL2", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*drt, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vL3", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*drt, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNL2", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*ndrt, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNL3", end='')
        print(rail, end='')
        print("\" \"", end='')
        print(*ndrf, sep="", end='')
        print("\")")
    elif wr_il_script == 2:
        print("if(schObjPropForm->instanceName->value == \"vL2", end = '')
        print(rail, end = '')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end = '')
        print(*drt, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vL3", end='')
        print(rail, end='')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*drf, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNL2", end='')
        print(rail, end='')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*ndrt, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNL3", end='')
        print(rail, end='')
        print("\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*ndrf, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")
    else:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Generate rails for rail-", rail)
        print("Single rail complete:", word)
        print("Single rail bit    n:", bitn)
        print("Single rail bit  n-1:", bitn1)
        print("----------------------------------")
        print()
        print("For bitn1:")
        print("Quad-rail normal true:  L2", rail)
        print(*drt, sep="")
        print("Quad-rail normal true:  L3", rail)
        print(*drf, sep="")
        print("Quad-rail invert true: NL2", rail)
        print(*ndrt, sep="")
        print("Quad-rail invert true: NL3", rail)
        print(*ndrf, sep="")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("")