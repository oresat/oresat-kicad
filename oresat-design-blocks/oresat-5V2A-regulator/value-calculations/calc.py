# Calculations for the capacitor and inductor values of the LTC3624-5 switching voltage regulator
# Datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/36242fd.pdf

from math import *
import textwrap

def linebreak(msg, newline=True, length=80):
    ''' Prints a line with the message, and the rest of the line is ===== '''
    m = f"== {msg} "
    while len(m) < length:
        m += '='
    if newline:
        print()
    print(m)

spscrnum = "⁰¹²³⁴⁵⁶⁷⁸⁹" # Footnote labels
footnotes = [] # The list of footnotes to print at the end
def footnote(note):
    ''' Returns a footnote label. The notes in the footnotes list must be printed at the end

    A maximum of 9 footnotes notes are allowed
    note is the text of the footnote
    returns a superscript number of the footnote that was just added '''
    if len(footnotes) > 9:
        raise IndexError('Too many footnotes')
        exit()
    footnotes.append(note)
    return spscrnum[len(footnotes)]

notes = [] # the not foot notes to print just before the footnotes

def prettyNum(num):
    ''' Takes a number, and converts it to unit prefix notation.

    Works for 1e-12(pico) <= num < 1e15(peta), otherwise just prints scienfic notation
    num is the number to prettify
    returns the number as a prettified string if possible '''
    if num < 1e3 and num >= 1:
        numstr = f"{num:.2f}"
        return f"{numstr.rstrip('0').rstrip('.') if '.' in numstr else numstr}"
    elif num >= 1e3 and num < 1e15:
        pos = 0
        while num > (1e3 - 1):
            num /= 1e3
            pos += 1
        numstr = f"{num:.2f}"
        return f"{numstr.rstrip('0').rstrip('.') if '.' in numstr else numstr}{' kMGT'[pos]}"
    elif num < 1 and num >= 1e-12:
        pos = 0
        while num < 1:
            num *= 1e3
            pos += 1
        numstr = f"{num:.2f}"
        return f"{numstr.rstrip('0').rstrip('.') if '.' in numstr else numstr}{' mμnp'[pos]}"
    else:
        return f"{num:.2e}"

def getFloat(msg, deflt, unit):
    ''' Gets a float from the user. If they don't enter anything, deflt is returned. unit is the unit string to print '''
    while True:
        i = input(f"{msg} ({prettyNum(deflt)}{unit}): ")
        if i == '':
            return deflt;
        try:
            f = float(i)
            return f
        except ValueError:
            print('Invalid value, please try again.')

# ================================================================
# Get the paramaters from the user, or use the defaults

linebreak("Config", False)
print('Paramaters to calculate values. Leave blank to accept default values.')
f = getFloat("Switching frequency", 1e6, 'Hz') # 1Mhz
vin = getFloat("Input voltage", 7.2, "V")
vinmax = getFloat("Max input voltage", 8.4, "V")
vout = getFloat("Output voltage", 5, "V")
ioutmax = getFloat("Maximum output current", 2, "A")
loadStepCurrent = getFloat("Load step", 2, "A")
vdroop = getFloat("Allowed output voltage droop at the step current change", 0.03*vout, "V")
outputRippleCurrent = getFloat("Output ripple current", 0.4*ioutmax, "A")

# ================================================================
# Calculates the component values
linebreak("Component values")

# input capacitor
notes.append("These calculations assumme creamic capacitors")
notes.append("When choosing the input and output ceramic capacitors, choose the X5R and X7R dielectric formulations")

irms = ioutmax * (vout/vin) * sqrt((vin/vout) - 1)
print(f"irms: {irms}")

cin = 10e-6
print(f"Cin: {prettyNum(cin)}F{footnote('This value is directly given by the datasheet as a reasonable choice.')}")

# output capacitor
cout = 3 * (loadStepCurrent / (f * vdroop))
print(f"Cout: {prettyNum(cout)}F{footnote('This value is stated as a good starting point, although more may be required depending on the duty cycle and load-step requirements')}")

# inductor
l = (vout / (f * outputRippleCurrent)) * (1 - (vout / vinmax))
print(f"L: {prettyNum(l)}H")

# ================================================================
# Print the notes
linebreak("Some notes from the datasheet")
wrapper = textwrap.TextWrapper(width=80, initial_indent="", subsequent_indent="   ")
for i in range(len(notes)):
    n = wrapper.wrap(f"*  {notes[i]}")
    for l in n:
        print(l)

# Print footnotes
linebreak("Footnotes")
for i in range(len(footnotes)):
    n = wrapper.wrap(f"{i+1:1}. {footnotes[i]}")
    for l in n:
        print(l)
