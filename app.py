import dearpygui.dearpygui as dpg
import sys
dpg.create_context()
dpg.create_viewport(title = "Heat Stress Index Research App", width=600,height=300)

measurements = []

def checklevel(level):
    if level < 40:
        print("The level is safe")
    elif level > 40 and level <= 59.9:
        print("Caution! ")
    elif level > 60 and level <= 79.9:
        print("Danger!")
    else:
        print("Extreme!")
def getinputs():
    day = dpg.get_value("day")
    temperature = dpg.get_value("temp")
    humidity = dpg.get_value("humidity")
    hsi = (0.7 * temperature) + (0.2 * humidity)
    grouped = [day,temperature,humidity,hsi]
    measurements.append(grouped)
    checklevel(hsi)
    # < 40 = safe, between 40 and 59.9 = caution, 60 and 79.9 = danger, and 80 or above = extreme
def open_data_entry():

    if dpg.does_item_exist("Data Entry"):
        dpg.delete_item("Data Entry")
    with dpg.window(tag="data_entry_window",label="Data Entry",width = 400,height=350,pos=[100,50]):
        dpg.add_text("Enter heat stress data.")
        dpg.add_separator()
        dpg.add_text("Day No.",)
        dpg.add_input_int(tag="day")
        dpg.add_text("Temperature")
        dpg.add_input_float(tag="temp")
        dpg.add_text("Humidity")
        dpg.add_input_float(min_value=0.0,tag="humidity")
        submit_btn = dpg.add_button(label="Yusuf wants to add something",callback=getinputs)
def view_data():
    if dpg.does_item_exist("Data View"):
        dpg.delete_item("Data View")
    with dpg.window(tag="data_view_window",label="Data View",width=400,weight=350,pos=[100,50]):
        dpg.add_text("Data View")

def exit():
    sys.exit("Exiting")

with dpg.window(tag="Window1"):
    dpg.add_text("HSI system")
    button1 = dpg.add_button(label="Data Entry",callback=open_data_entry,)
    button2 = dpg.add_button(label="Data View",callback=view_data)
    #exit button
    button3 = dpg.add_button(label="Exit",callback=exit,user_data="Value is passed")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Window1",True) #keeps it in a singular one
dpg.start_dearpygui()
dpg.destroy_context()
