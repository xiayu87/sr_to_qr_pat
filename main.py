import sys
from single_to_quad_rail_pattern import gen_sr_qr
from single_to_dual_rail_rack import gen_ctrl
from wr_il_fun_modinrails import pr_il_modinrails
from single_to_quad_rail_select import gen_qrsel
from single_to_dual_rail_select import gen_drsel

"Set variables for scenarios"
"---------------------------"
"wr_il_script; select 1 if require Skill script output"
"wr_il_script; select 0 if do not require Skill script output"
wr_il_script = 0
"Specify the rails of select signals, dual or quad"
sel_rail_type = "quad";
"Enter the select signals based on the rail"
sel_wires = [3, 2, 4, 1]
"Specify Cadence library, cell details"
lib = "lib"
cell = "cell"




if wr_il_script == 1:
    sys.stdout = open("single_to_quad_rail_pattern.il", "wt")
    pr_il_modinrails(wr_il_script)
elif wr_il_script == 2:
    print("write complete Skill script")
    sys.stdout = open("single_to_quad_rail_pattern_new.il", "wt")
    pr_il_modinrails(wr_il_script)
else:
    print("Running code without writing Skill script")
    sys.stdout = open("single_to_quad_rail_pattern.txt", "wt")

"Specify rails and their lists"
"============================="
"Data input 1"
lx1 = [1, 0, 0, 1, 0, 0, 1, 0]
gen_sr_qr(lx1, 0, wr_il_script)

"Data input 2"
lx2 = [1, 1, 0, 0, 0, 0, 1, 1]
gen_sr_qr(lx2, 1, wr_il_script)

"Data input 3"
lx3 = [0, 1, 1, 0, 1, 0, 0, 1]
gen_sr_qr(lx3, 2, wr_il_script)

"Data input 4"
lx4 = [0, 0, 1, 1, 0, 1, 0, 0]
gen_sr_qr(lx4, 3, wr_il_script)
"============================"
"End of rails and their lists"

"Rack signal based on the length of data rails"
lx1_len = len(lx1)
gen_ctrl(lx1_len, wr_il_script)

if sel_rail_type == "quad":
    gen_qrsel(sel_wires, wr_il_script)
elif sel_rail_type == "dual":
    gen_drsel(sel_wires)
else:
    print("Wrong select signal rail type")

if wr_il_script == 2:
    print(")")
    print(")")
    print(")")
    print("modinrails(\"bb_sahb_work\" \"mux_QR_SAHB_TEST\")")