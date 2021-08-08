"""

This script creates a GUI miles to kilometers/meters converter.

This script requires that 'tkinter' be installed within the Python
environment you are running this script in.

"""

import tkinter

FONT = ('Arial', 10, 'bold')

window = tkinter.Tk()
window.title(string='Mile to Km Converter')
window.minsize(width=300, height=200)
window.config(padx=75, pady=50)


def convert_miles():
    """Takes the amount of miles and coverts it to kilometers or meters
    and updates the GUI to display the conversion
    """
    if radio_state.get() == 0:
        miles = float(miles_entry.get())
        kilometers = round(miles * 1.60934, ndigits=2)
        miles_converted_label.config(text=kilometers)
        final_conversion_unit_label.config(text='kilometers')
    else:
        miles = float(miles_entry.get())
        m = round(miles * 1609.4, ndigits=2)
        miles_converted_label.config(text=m)
        final_conversion_unit_label.config(text='meters')


miles_label = tkinter.Label()
miles_label.grid(row=1, column=3)
miles_label.config(text='Miles', font=FONT)

final_conversion_unit_label = tkinter.Label()
final_conversion_unit_label.grid(row=2, column=3)
final_conversion_unit_label.config(text='?', font=FONT)

equal_label = tkinter.Label()
equal_label.grid(row=2, column=1)
equal_label.config(text='is equal to', font=FONT)

miles_converted_label = tkinter.Label()
miles_converted_label.grid(row=2, column=2)
miles_converted_label.config(text=0)

calculate_button = tkinter.Button()
calculate_button.grid(row=3, column=2)
calculate_button.config(text='Calculate', font=FONT, command=convert_miles)

miles_entry = tkinter.Entry()
miles_entry.grid(row=1, column=2)
miles_entry.config(width=10, text=0)

radio_state = tkinter.IntVar()

km_radiobutton = tkinter.Radiobutton(variable=radio_state, value=0)
km_radiobutton.grid(row=1, column=4)

m_radiobutton = tkinter.Radiobutton(variable=radio_state, value=1)
m_radiobutton.grid(row=2, column=4)

options_label = tkinter.Label(text='Convert to?')
options_label.grid(row=0, column=4)

km_label = tkinter.Label(text='km')
km_label.grid(row=1, column=5)

m_label = tkinter.Label(text='m')
m_label.grid(row=2, column=5)

window.mainloop()