def gen_ctrl(numbits, wr_il_script):

    rack = [0] * numbits
    nrack = [0] * numbits

    z = numbits - 1

    while z >= 0:
        rack[z] = 0
        rack[z-1] = 1

        nrack[z] = 1
        nrack[z-1] = 0

        z = z - 2

    if wr_il_script == 1:
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vRACK\" \"", end='')
        print(*rack, sep="", end='')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNRACK\" \"", end='')
        print(*nrack, sep="", end='')
        print("\")")
    elif wr_il_script == 2:
        print("if(schObjPropForm->instanceName->value == \"vRACK\"")
        print("then")
        print("schObjPropForm->data->value=\"", end = '')
        print(*rack, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNRACK\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*nrack, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")
    else:
        print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
        print("The control signals")
        print("Rack:")
        print(*rack, sep="")
        print("Rack:")
        print(*nrack, sep="")
        print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")