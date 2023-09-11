def gen_qrsel(pattern, wr_il_script):

    "Pattern example pattern=1234"
    wordlength = len(pattern)
    raillength = (wordlength * 2)
    railiterat = wordlength - 1

    sel0 = [0] * raillength
    sel1 = [0] * raillength
    sel2 = [0] * raillength
    sel3 = [0] * raillength
    nsel0 = [0] * raillength
    nsel1 = [0] * raillength
    nsel2 = [0] * raillength
    nsel3 = [0] * raillength

    raillength = raillength - 1

    while railiterat >= 0:
        if pattern[railiterat] == 1:
            sel0[raillength] = 1
            sel1[raillength] = 0
            sel2[raillength] = 0
            sel3[raillength] = 0
            nsel0[raillength] = 0
            nsel1[raillength] = 1
            nsel2[raillength] = 1
            nsel3[raillength] = 1
        elif pattern[railiterat] == 2:
            sel0[raillength] = 0
            sel1[raillength] = 1
            sel2[raillength] = 0
            sel3[raillength] = 0
            nsel0[raillength] = 1
            nsel1[raillength] = 0
            nsel2[raillength] = 1
            nsel3[raillength] = 1
        elif pattern[railiterat] == 3:
            sel0[raillength] = 0
            sel1[raillength] = 0
            sel2[raillength] = 1
            sel3[raillength] = 0
            nsel0[raillength] = 1
            nsel1[raillength] = 1
            nsel2[raillength] = 0
            nsel3[raillength] = 1
        elif pattern[railiterat] == 4:
            sel0[raillength] = 0
            sel1[raillength] = 0
            sel2[raillength] = 0
            sel3[raillength] = 1
            nsel0[raillength] = 1
            nsel1[raillength] = 1
            nsel2[raillength] = 1
            nsel3[raillength] = 0

        sel0[raillength-1] = 0
        sel1[raillength-1] = 0
        sel2[raillength-1] = 0
        sel3[raillength-1] = 0
        nsel0[raillength-1] = 1
        nsel1[raillength-1] = 1
        nsel2[raillength-1] = 1
        nsel3[raillength-1] = 1

        railiterat = railiterat - 1
        raillength = raillength - 2

    if wr_il_script == 1:
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vS0\" \"", end = '')
        print(*sel0, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vS1\" \"", end = '')
        print(*sel1, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vS2\" \"", end = '')
        print(*sel2, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vS3\" \"", end = '')
        print(*sel3, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNS0\" \"", end = '')
        print(*nsel0, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNS1\" \"", end = '')
        print(*nsel1, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNS2\" \"", end = '')
        print(*nsel2, sep="", end = '')
        print("\")")
        print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\" \"vNS3\" \"", end = '')
        print(*nsel3, sep="", end = '')
        print("\")")
    elif wr_il_script == 2:
        print("if(schObjPropForm->instanceName->value == \"vS0\"")
        print("then")
        print("schObjPropForm->data->value=\"", end = '')
        print(*sel0, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vS1\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*sel1, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vS2\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*sel2, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vS3\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*sel3, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNS0\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*nsel0, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNS1\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*nsel1, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNS2\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*nsel2, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")

        print("if(schObjPropForm->instanceName->value == \"vNS3\"")
        print("then")
        print("schObjPropForm->data->value=\"", end='')
        print(*nsel3, sep="", end='')
        print("\"")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")
    else:
        print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        print("Select signals for 4-to-1 Quad-rail Mux")
        print("Quad-rail normal select:  Sx")
        print(*sel0, sep="")
        print("Quad-rail normal select:  Sx")
        print(*sel1, sep="")
        print("Quad-rail normal select:  Sx")
        print(*sel2, sep="")
        print("Quad-rail normal select:  Sx")
        print(*sel3, sep="")
        print("Quad-rail invert select: NSx")
        print(*nsel0, sep="")
        print("Quad-rail invert select: NSx")
        print(*nsel1, sep="")
        print("Quad-rail invert select: NSx")
        print(*nsel2, sep="")
        print("Quad-rail invert select: NSx")
        print(*nsel3, sep="")
        print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")