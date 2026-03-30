import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title = "Heat Stress Index Research App", width=600,height=300)

with dpg.window(label="Test 1"):
    dpg.add_text("Heat Stress Index Research App")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()