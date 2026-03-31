import dearpygui.dearpygui as dpg
import sys
dpg.create_context()
dpg.create_viewport(title = "Heat Stress Index Research App", width=600,height=300)

def exit(sender,user_data):
    sys.exit("Exiting")

with dpg.window(tag="Window1"):
    dpg.add_text("Heat Stress Index Research App")
    button1 = dpg.add_button(label="Data Entry",callback=dataEntry,user_data="Data Entry")
    button2 = dpg.add_button(label="Data View")
    button3 = dpg.add_button(label="Exit",callback=exit,user_data="user exit")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Window1",True) #keeps it in a singular one
dpg.start_dearpygui()
dpg.destroy_context()