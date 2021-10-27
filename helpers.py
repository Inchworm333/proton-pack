#helpers.py
#has helper functions that might be needed in more than one file.

def mode_decode(modeID):
    inner_mode = modeID % 4
    
    if inner_mode == 0:
        #Proton
        return "proton"
    elif inner_mode == 1:
        #Slime
        return "slime"
    elif inner_mode == 2:
        #Stasis
        return "stasis"
    elif inner_mode == 3:
        #Meson
        return "meson"
