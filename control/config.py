from otree.api import BaseConstants, Currency


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):

    name_in_url = 'control'
    players_per_group = 3

    num_rows = 10
    num_cols = 10

    risks = [1, 5, 10]

    stakes = 500

    # box height and box width in pixels
    # make sure that the size of the boxes fits the screen of the device
    # note that the layout is responsive, i.e. boxes will break into new rows if they don't fit
    box_height = '50px'
    box_width = '50px'

    # number of rounds to be played
    num_rounds = 5


