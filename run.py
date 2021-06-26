import os
import tkinter
from tkinter import filedialog
import time
import click


def generate_gcode(serial_number):
    length_counter = 0;
    characters = list(serial_number)
    print(characters)
    cwd = os.getcwd()
    input_dir = tkinter.Tk()
    input_dir.withdraw()
    # pick up the Input file path
    print("Please select the input files directory")
    print("---------------------------------------\n")
    time.sleep(1)
    tempdir = filedialog.askdirectory(parent=input_dir, initialdir=cwd, title='Please select a directory')
    if len(tempdir) > 0:
        if '\\' in tempdir:
            tempdir = tempdir + '\\'
        else:
            tempdir = tempdir + '/'
        print("You choose:\n", tempdir)



@click.command()
@click.option('--serial_number', prompt='Enter the serial number', help='Battery Serial Number')
def get_input_from_user(serial_number):
    click.echo('Thank you for your input!')
    generate_gcode(serial_number)



def main():
    get_input_from_user()


if __name__ == "__main__":
    main()
