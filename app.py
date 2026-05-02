'''
Climate Application

Author: @Carlos Raniel Ariate Arro
Co-Author(s): @Zain Azrak @Yusuf Bouaouina

Description:
Desktop-based Heat Stress Index (HSI) system developed to analyse
environmental conditions in a desert climate using Dear PyGui.
'''

# =========================
# IMPORTS
# =========================
import csv
import os
import sys
import dearpygui.dearpygui as dpg

# =========================
# DPG SETUP
# =========================
dpg.create_context()
dpg.create_viewport(
    title="Heat Stress Index Research App",
    width=800,
    height=600
)

# =========================
# THEME
# =========================
with dpg.theme() as my_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10)
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)

# =========================
# CLASS
# =========================
class Measurement:

    def __init__(self, dayNo, temp, humidity, HSI=0, RL="Unknown"):
        self.dayNo = dayNo
        self.temp = temp
        self.humidity = humidity
        self.HSI = HSI
        self.RL = RL

    # Calculate Heat Stress Index
    def calculateHSI(self):
        self.HSI = (0.7 * self.temp) + (0.2 * self.humidity)
        return self.HSI

    # Classify HSI Risk Level
    def classifyHSI(self):

        if self.HSI < 40:
            self.RL = "Safe"

        elif 40 <= self.HSI <= 59.9:
            self.RL = "Caution"

        elif 60 <= self.HSI <= 79.9:
            self.RL = "Danger"

        else:
            self.RL = "Extreme"

        return self.RL

# =========================
# GLOBAL DATA STORAGE
# =========================
dataReadings = []

# =========================
# FILE FUNCTIONS
# =========================
def getFromFile():

    filename = "HSI_Data.csv"

    if os.path.isfile(filename):

        with open(filename, mode='r') as file:
            csvFile = csv.reader(file)
            return list(csvFile)

    else:
        return [["Error: File does not exist"]]

def putInfile(dataReadings):

    if not dataReadings:
        return "Error: No data to save"

    filename = "HSI_Data.csv"

    fields = [
        'Day Number',
        'Temperature',
        'Humidity',
        'Heat Stress Index',
        'Risk Level'
    ]

    rows = [
        [m.dayNo, m.temp, m.humidity, m.HSI, m.RL]
        for m in dataReadings
    ]

    with open(filename, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    return "Data saved successfully"

# =========================
# EDA FUNCTIONS
# =========================
def calculateAverage(dataReadings):

    if not dataReadings:
        return "Error: No data"

    avg = sum(m.HSI for m in dataReadings) / len(dataReadings)

    return f"Average HSI: {avg:.2f}"

def getHighest(dataReadings):

    if not dataReadings:
        return "Error: No data"

    maxM = max(dataReadings, key=lambda m: m.temp)

    return f"Highest Temperature: {maxM.temp} on Day {maxM.dayNo}"

def countExtreme(dataReadings):

    if not dataReadings:
        return "Error: No data"

    count = sum(1 for m in dataReadings if m.RL == "Extreme")

    return f"Extreme Risk Count: {count}"

# =========================
# DATA INPUT FUNCTION
# =========================
def DataInput():

    day = dpg.get_value("day")
    temp = dpg.get_value("temp")
    humidity = dpg.get_value("humidity")

    # validation
    if day <= 0:
        dpg.set_value("status", "Day number must be greater than 0")
        return

    m = Measurement(day, temp, humidity)

    m.calculateHSI()
    m.classifyHSI()

    dataReadings.append(m)

    dpg.set_value(
        "status",
        f"Day {day} added | Temp={temp}°C | Humidity={humidity}% | "
        f"HSI={m.HSI:.2f} | Risk={m.RL}"
    )

    # auto refresh table
    ViewData()

# =========================
# SAVE FUNCTION
# =========================
def SaveData():

    msg = putInfile(dataReadings)

    dpg.set_value("status", msg)

# =========================
# VIEW DATA FUNCTION
# =========================
def ViewData():
    # Mock data (2D Array)
    mock_data = [
        [1, 34.5, 45.0, 33.15, "Safe"],
        [2, 39.2, 50.0, 37.44, "Safe"],
        [3, 42.0, 65.0, 42.40, "Caution"],
        [4, 48.3, 70.0, 47.81, "Caution"],
        [5, 55.0, 72.0, 52.90, "Caution"],
        [6, 61.0, 75.0, 57.70, "Caution"],
        [7, 68.0, 80.0, 63.60, "Danger"],
        [8, 72.5, 82.0, 67.15, "Danger"],
        [9, 78.0, 85.0, 71.60, "Danger"],
        [10, 85.0, 90.0, 77.50, "Danger"],
        [11, 92.0, 95.0, 83.40, "Extreme"],
        [12, 100.0, 98.0, 89.60, "Extreme"]
    ]
    # clear previous rows
    if dpg.does_item_exist("table_rows"):
        dpg.delete_item("table_rows")

    with dpg.group(tag="table_rows", parent="data_table"):

        for m in dataReadings:

            with dpg.table_row():

                dpg.add_text(str(m.dayNo))
                dpg.add_text(f"{m.temp}")
                dpg.add_text(f"{m.humidity}")
                dpg.add_text(f"{m.HSI:.2f}")
                dpg.add_text(m.RL)

# =========================
# RUN EDA
# =========================
def RunEDA():

    avg = calculateAverage(dataReadings)
    high = getHighest(dataReadings)
    extreme = countExtreme(dataReadings)

    dpg.set_value(
        "eda_output",
        f"{avg}\n{high}\n{extreme}"
    )

    dpg.configure_item("eda_window", show=True)

# =========================
# EXIT FUNCTION
# =========================
def ExitApp():
    sys.exit("Exiting")

# =========================
# MAIN WINDOW
# =========================
with dpg.window(tag="MainWindow"):

    dpg.add_text("Heat Stress Index System")

    dpg.add_separator()

    dpg.add_button(
        label="Data Entry",
        callback=lambda: dpg.configure_item(
            "data_entry_window",
            show=True
        )
    )

    dpg.add_button(
        label="Data View",
        callback=lambda: dpg.configure_item(
            "data_view_window",
            show=True
        )
    )

    dpg.add_button(
        label="Run EDA",
        callback=RunEDA
    )

    dpg.add_button(
        label="Save to CSV",
        callback=SaveData
    )

    dpg.add_button(
        label="Exit",
        callback=ExitApp
    )

    dpg.add_separator()

    dpg.add_text("", tag="status")

# =========================
# DATA ENTRY WINDOW
# =========================
with dpg.window(
    tag="data_entry_window",
    label="Data Entry",
    show=False,
    width=400,
    height=350,
    pos=[50, 50]
):

    dpg.add_text("Enter heat stress data")
    dpg.add_separator()

    dpg.add_text("Day Number")
    dpg.add_input_int(tag="day")

    dpg.add_text("Temperature")
    dpg.add_input_float(tag="temp")

    dpg.add_text("Humidity")
    dpg.add_input_float(
        tag="humidity",
        min_value=0.0,
        max_value=100.0
    )

    dpg.add_separator()

    dpg.add_button(
        label="Submit",
        callback=DataInput
    )

# =========================
# DATA VIEW WINDOW
# =========================
with dpg.window(
    tag="data_view_window",
    label="Data View",
    show=False,
    width=600,
    height=400,
    pos=[200, 50]
):

    dpg.add_text("Recorded Heat Stress Data")

    with dpg.table(
        tag="data_table",
        header_row=True,
        borders_innerH=True,
        borders_outerH=True,
        borders_innerV=True,
        borders_outerV=True
    ):

        dpg.add_table_column(label="Day")
        dpg.add_table_column(label="Temperature")
        dpg.add_table_column(label="Humidity")
        dpg.add_table_column(label="HSI")
        dpg.add_table_column(label="Risk Level")

# =========================
# EDA WINDOW
# =========================
with dpg.window(
    tag="eda_window",
    label="EDA Results",
    show=False,
    width=400,
    height=200,
    pos=[250, 150]
):

    dpg.add_text("", tag="eda_output")

# =========================
# APPLY THEME
# =========================
dpg.bind_theme(my_theme)

# =========================
# DPG STRUCTURE
# =========================
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("MainWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()