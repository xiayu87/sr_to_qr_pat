"print skill function to modify voltage parameters according to quad-rail"

def pr_il_modinrails(wr_il_script):
    if wr_il_script == 1:
        print("procedure(modinrails(lib cell vinst prail)")
        print("let((cv newLabel)")
        print("cv = dbOpenCellViewByType(lib cell \"schematic\" \"\" \"a\")")
        print("foreach(instance cv~>instances")
        print("geSelectObjectNoFilter(instance)")
        print("schHiObjectProperty()")
        print("if(schObjPropForm->instanceName->value == vinst")
        print("then")
        print("schObjPropForm->data->value=prail")
        print(")")
        print("hiFormDone(schObjPropForm)")
        print("geDeselectAll()")
        print(")")
        print(")")
        print(")")
    elif wr_il_script == 2:
        print("procedure(modinrails(lib cell)")
        print("let((cv newLabel)")
        print("cv = dbOpenCellViewByType(lib cell \"schematic\" \"\" \"a\")")
        print("foreach(instance cv~>instances")
        print("geSelectObjectNoFilter(instance)")
        print("schHiObjectProperty()")