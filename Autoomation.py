import webbrowser

print('Welcome to the Automation project made by Sourav')

subject=input('Enter the class you have now:')

if subject=='computer science':
    webbrowser.open('https://us04web.zoom.us/j/5695479354?pwd=RVNrak92R3hPb1RLQitKVCtadHZtUT09')
    print('you have entered the ',subject,'class successfully')

elif subject=='english':
    webbrowser.open('https://us04web.zoom.us/j/3087645148?pwd=Wk12TXo2YWNpWkltNHlYdmNGMk5XZz09')
    print('you have entered the ',subject,'class successfully')

elif subject=='maths':
    webbrowser.open('https://us04web.zoom.us/j/4796192771?pwd=aHBzOTl5cERjVU1iYUpDMXg3YmJWZz09')
    print('you have entered the ',subject,'class successfully')

elif subject=='chemistry':
    webbrowser.open('https://us04web.zoom.us/j/73776839146?pwd=N25MU09FRndVY2tQeHB0L1I0VmEyQT09')
    print('you have entered the ',subject,'class successfully')

elif subject=='physics':
    webbrowser.open('https://us04web.zoom.us/j/4728270497?pwd=OENoTHdrbnJSeUtFcTZnclhqQ09YUT09')
    print('you have entered the ',subject,'class successfully')
else:
    print('You have entered wrong subject ')

