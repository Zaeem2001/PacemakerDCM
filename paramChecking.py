# PARAMETER VALIDITY CHECKS
def check_LRL(lrlval):
    errormsg = ""
    error = False

    if (lrlval > 175 or lrlval < 30):
        error = True
        errormsg = "        Please make sure the LRL value          \n           is between 30-175 ppm.        "

    elif (lrlval >= 30 and lrlval <= 50 and (lrlval % 5 != 0)):
        error = True
        errormsg = "        Please make sure the increment LRL         \n         by 5 ppm for vals of 30-50 ppm.        "

    elif (lrlval >= 90 and lrlval <= 175 and (lrlval % 5 != 0)):
        error = True
        errormsg = "        Please make sure the increment LRL         \n         by 5 ppm for vals of 90-175 ppm.        "

    return error, errormsg

def check_URL(urlval, lrlval):
    errormsg = ""
    error = False

    if (urlval > 175 or urlval < 50 or urlval % 5 != 0):
        error = True
        errormsg = "        Please make sure the URL value          \n         is between 50-175 ppm, incremented by 5ppm.        "

    if (lrlval >= urlval):
        error = True
        errormsg = "        Please make sure the LRL value          \n         is less than the URL value.        "

    return error, errormsg

def check_AA(aaval):
    errormsg = ""
    error = False

    if (aaval < 0 or aaval > 5 or (aaval * 100) % 10 != 0):
        error = True
        errormsg = "        Please make sure the AA value         \n         is between 0 and 5 V, incremented by 0.1 V.        "

    return error, errormsg

def check_VA(vaval):
    errormsg = ""
    error = False

    if (vaval < 0 or vaval > 5 or (vaval * 100) % 10 != 0):
        error = True
        errormsg = "        Please make sure the VA value         \n         is between 0 and 5 V, incremented by 0.1 V.        "

    return error, errormsg

def check_APW(apwval):
    errormsg = ""
    error = False

    if (apwval > 30 or apwval < 1):
        error = True
        errormsg = "        Please make sure the APW value is between         \n         1 and 30ms, incremented by 1ms.        "

    return error, errormsg

def check_VPW(vpwval):
    errormsg = ""
    error = False

    if (vpwval > 30 or vpwval < 1):
        error = True
        errormsg = "        Please make sure the VPW value is between         \n         1 and 30ms, incremented by 1ms.        "

    return error, errormsg

def check_ARP(lrlval, arpval):
    errormsg = ""
    error = False

    if (not (arpval >= 10 and arpval <= 500 and (arpval % 10 == 0))):
        error = True
        errormsg = "        Please make sure the ARP value is between          \n         150-500ms, incremented by 10ms.        "

    elif (60000/lrlval <= arpval):
        error = True
        errormsg = "        Please make sure the LRL value in ms      \n         is greater than the ARP value.        "

    return error, errormsg

def check_VRP(lrlval, vrpval):
    errormsg = ""
    error = False

    if (not (vrpval >= 150 and vrpval <= 500 and (vrpval % 10 == 0))):
        error = True
        errormsg = "        Please make sure the VRP value is between          \n         150-500ms, incremented by 10 ms.        "

    elif (60000/lrlval <= vrpval):
        error = True
        errormsg = "        Please make sure the LRL value in ms      \n         is greater than the VRP value.        "

    return error, errormsg

def check_MAX_SENSE_RATE(max, urlval, lrlval):
    errormsg = ""
    error = False

    if (max > 175 or max < 50 or max % 5 != 0):
        error = True
        errormsg = "        Please make sure the maximum sensor rate value         \n         is between 50-175 ppm, incremented by 5ppm.        "

    elif (max > urlval):
        error = True
        errormsg = "        Please make sure the maximum sensor rate value         \n         is less than the URL value.        "

    elif (max < lrlval):
        error = True
        errormsg = "        Please make sure the maximum sensor rate value         \n         is greater than the LRL value.        "

    return error, errormsg

def check_AV_DELAY(delay):
    errormsg = ""
    error = False

    if (delay > 300 or delay < 70 or delay % 10 != 0):
        error = True
        errormsg = "        Please make sure the fixed AV delay value        \n         is between 70-300 ms, incremented by 10ppm.        "

    return error, errormsg

def check_AS (sensitivity):
    errormsg = ""
    error = False

    if (sensitivity > 5 or sensitivity < 0 or (sensitivity * 100) % 10 != 0):
        error = True
        errormsg = "        Please make sure the atrial sensitivity value         \n         is between 0-5 V, incremented by 0.1V.        "

    return error, errormsg

def check_VS (sensitivity):
    errormsg = ""
    error = False

    if (sensitivity > 5 or sensitivity < 0 or (sensitivity * 100) % 10 != 0):
        error = True
        errormsg = "        Please make sure the ventricular sensitivity value         \n         is between 0-5 V, incremented by 0.1V.        "

    return error, errormsg

def check_PVARP(pvarp):
    errormsg = ""
    error = False

    if (pvarp > 500 or pvarp < 150 or pvarp % 10 != 0):
        error = True
        errormsg = "        Please make sure the PVARP value         \n         is between 150-500ms, incremented by 10ms.        "

    return error, errormsg


def check_RXN_TIME(rxn):
    errormsg = ""
    error = False

    if (rxn > 50 or rxn < 10 or rxn % 10 != 0):
        error = True
        errormsg = "        Please make sure the reaction time         \n         is between 10-50s, incremented by 10s.        "

    return error, errormsg

def check_RESPONSE(response):
    errormsg = ""
    error = False

    if (response > 16 or response < 1):
        error = True
        errormsg = "        Please make sure the response factor         \n         is between 1-16, incremented by 1.        "

    return error, errormsg

def check_RECOVERY(recovery):
    errormsg = ""
    error = False

    if (recovery > 16 or recovery < 2):
        error = True
        errormsg = "        Please make sure the recovery time         \n         is between 2-16 minutes, incremented by 1 minute.        "

    return error, errormsg