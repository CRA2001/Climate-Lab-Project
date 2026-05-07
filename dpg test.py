import dearpygui.dearpygui as dpg

dpg.create_context()

dpg.create_viewport(
    title="Heat Stress Index Research App",
    width=800,
    height=600
)

with dpg.window(tag="MainWindow"):

    dpg.add_text("Heat Stress Index System")

    dpg.add_separator()

    with dpg.group(horizontal=True):

        dpg.add_button(
            label="Data Entry",
            show=True
        )

        dpg.add_button(
            label="Data View",
        )

        dpg.add_button(
            label="Run EDA",
        )

    dpg.add_button(
        label="Save to CSV",
    )

    dpg.add_button(
        label="Exit",
    )

    dpg.add_separator()

    dpg.add_text("", tag="status")

# =========================
# DPG STRUCTURE
# =========================
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("MainWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()