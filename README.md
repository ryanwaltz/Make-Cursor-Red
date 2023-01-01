# Make-Cursor-Red

This is a simple program to change the cursor color on Google Docs. While in school, I noticed that although many assignments required you to change the text color to red, there is no keybaord shortcut so you are forced to move your cursor each time. 

To rectify this, I made a program which can find the two buttons required to change the cursor color. The program waits for an input by the user, typically "`", and measures the position of the cursor. This is assumed to be the button which opens the menu to the color select. The position of the red color in comparision to the the button which opens the menu.

After the calibration, all the user needs to do is press the input ("`") and the cursor will be changed to red.

This does not work with selected text, and only serves to make the cursor red. 

The modules that are used are the keyboard module and the pynput module. Both can be installed on all (osx and windows tested) platforms.
