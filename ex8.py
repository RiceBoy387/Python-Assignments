# Creat the LightSwitch class
class LightSwitch:
    '''A class to represent a light switch'''

    def __init__(self, state):
        '''(LightSwitch, bool) -> NoneType
        Create a switch that is either ON equivalent to True and OFF which
        will be equivalent to False
        REQ: boolean representation of on or off
        '''
        if (state == "on"):
            self._state = True
        else:
            self._state = False

    def __str__(self):
        '''(LightSwitch) -> str
        Create the string output when user wants to print the current state
        '''
        # Initialize the return variable
        output = ""
        # If statement to determine what the output should be
        if (self._state == 0):
            output = "I am off"
        else:
            output = "I am on"
        # Return the state
        return output

    # Turn on method
    def turn_on(self):
        # Use if statement to make sure that the state is False/off before
        # turning it on
        if (self._state == 0):
            self._state = True

    # Turn off method
    def turn_off(self):
        # Use if statement to make sure that the state is True/on before
        # turning it off
        if (self._state == 1):
            self._state = False

    # Flip Method
    def flip(self):
        # If statement to detemrine the current state and flip it
        if (self._state == 0):
            self._state = True
        else:
            self._state = False


# Create the SwitchBoard class
class SwitchBoard:

    def __init__(self, num_of_switch):
        '''(SwitchBoard, int) -> NoneType
        This method is designed to create a switchboard given the number
        of switches as set by the user
        REQ: the number of switches must be a valid integer >= 0
        '''
        self._switchboard = []
        self._num_of_switches = num_of_switch
        # Use a loop to create a list of all the switches and set them to off
        for index in range(self._num_of_switches):
            self._switchboard.append(False)

    def __str__(self):
        '''(SwitchBoard) -> str
        Create a string output when the user wants to see what switches are on
        '''
        whats_on = "The following switches are on: "
        # Call the method which creates the list of switches that are on
        self.which_switch()
        self._list_of_on = self._on_switches
        # Use a loop to go through the list and concatenate a string output
        for index in range(len(self._list_of_on)):
            light = str(self._list_of_on[index])
            whats_on += (light + " ")
        return whats_on

    # Method to turn off all the switches
    def reset(self):
        '''(Switchboard) -> NoneType
        This method is to reset the switch board (Turn off all the switches)
        '''
        # Use a loop to go through the board and switch everything off
        for index in range(len(self._switchboard)):
            self._switchboard[index] = False

    # Method for returning the switches that are on
    def which_switch(self):
        '''(Switchboard) -> list
        This method is designed to go through the switch board and
        put all the switches that are on into another list to be returned
        '''
        # Create a list to store all the switches that are on
        self._on_switches = []
        # Use a loop to go through the switchboard and see which are on
        # Put the index of the ones that are on into a new list
        for switch in range(len(self._switchboard)):
            if (self._switchboard[switch] == 1):
                self._on_switches.append(switch)
        return self._on_switches

    # Single flip switch method
    def flip(self, switch):
        '''(SwithBoard, int) -> NoneType
        This method is designed to turn off the switch specified by the user
        '''
        # Make sure the switch actually exists so doesn't crash
        if (len(self._switchboard) >= switch):
            # If statement to detemine the state of the switch and flip
            # it accordingly
            if (self._switchboard[switch] == 1):
                self._switchboard[switch] = 0
            else:
                self._switchboard[switch] = 1

    # Flip every ____ st,nd,rd switch method
    def flip_every(self, skip):
        '''(SwitchBoard, int) -> NoneType
        This method is designed to flip the switches skipping the specified
        number by the user
        '''
        # To prevent an error where skip cant be equal to 0
        if (skip == 0):
            skip = 1

        # Loop with the skip condition
        for index in range(0, len(self._switchboard), skip):
            # If statement to flip the desired switches
            if (self._switchboard[index] == 1):
                self._switchboard[index] = 0
            else:
                self._switchboard[index] = 1


if(__name__ == "__main__"):
    switch_board = SwitchBoard(1023)
    # Use a loop to continuosly increase the skip number when flipping the
    # switches
    for index in range(1023):
        switch_board.flip_every(index+1)
