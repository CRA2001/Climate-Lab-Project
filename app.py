import dearpygui.dearpygui as dpg
import sys
dpg.create_context()
dpg.create_viewport(title = "Heat Stress Index Research App", width=600,height=300)


def open_data_entry(sender,user_data):
    if dpg.does_item_exist("data_entry_window"):
        dpg.delete_item("data entry window")
    with dpg.window(tag="data_entry_window",label="Data Entry",width = 400,height=350,pos=[100,50]):
        dpg.add_text("Enter heat stress data.")
        dpg.add_separator()
def exit(sender,user_data):
    sys.exit("Exiting")

with dpg.window(tag="Window1"):
    dpg.add_text("Heat Stress Index Research App")
    button1 = dpg.add_button(label="Data Entry",callback=open_data_entry,user_data="data_entry")
    button2 = dpg.add_button(label="Data View")
    #exit button
    button3 = dpg.add_button(label="Exit",callback=exit,user_data="user exit")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Window1",True) #keeps it in a singular one
dpg.start_dearpygui()
dpg.destroy_context()