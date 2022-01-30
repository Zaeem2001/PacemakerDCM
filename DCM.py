from pmParams import *
from nav import *
from serialcom import *

class DCM():
	# SET UP DCM PAGE
    def __init__(self, parent, *args, **kwargs):
        DCM = parent
        DCM.geometry("980x720")
        DCM.title("DCM")
        ser = serialcom()

        navFrm = Frame(DCM)
        navWnd = nav(navFrm, DCM, args[0], ser)

        pmParamsFrm = Frame(DCM)
        pmParamsWnd = pmParams(pmParamsFrm, args[0], ser, DCM)