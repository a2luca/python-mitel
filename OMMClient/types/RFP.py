from threading import Lock


class RFP:
    """
    Class representing a RFP (Radio Fixed Part) in the SIP-DECT OM Application XML Interface.
    :type _ommclient: OMMClient
    :param _ommclient: OMM Client

    :type id: int
    :param id: Unique RFP identifier. The numbering starts at 0

    :type ethAddr: str
    :param ethAddr: Ethernet address, format "00:11:22:aa:bb:cc"

    :type dectOn: bool
    :param dectOn: True if DECT is enabled on this RFP

    :type wlanOn: bool
    :param wlanOn: True if WLAN is enabled on this RFP

    :type licenseRfp: bool
    :param licenseRfp: This RFP is used for licensing, it cannot be deleted

    :type name: str
    :param name: Name of this RFP, free format text.

    :type hierarchy1: str
    :param hierarchy1: Position hierarchy level 1, free format text

    :type hierarchy2: str
    :param hierarchy2: Position hierarchy level 2, free format text

    :type hierarchy3: str
    :param hierarchy3: Position hierarchy level 3, free format text

    :type hierarchy4: str
    :param hierarchy4: Position hierarchy level 4, free format text

    :type rpn: int
    :param rpn: DECT RPN

    :type pagingArea: int
    :param pagingArea: Paging area number, -1 for unassigned

    :type cluster: int
    :param cluster: Synchronization cluster, 0 is invalid

    :type preferredSync: bool
    :param preferredSync: This RFP is preferred in sync start up

    :type reflectiveEnv: bool
    :param reflectiveEnv: This RFP is located in a reflective environment

    :type site: int
    :param site: Reference to site data set id.

    :type x: int
    :param x: X coordinate for visualization

    :type y: int
    :param y: Y coordinate for visualization

    :type hwType: RFPHwTypeType
    :param hwType: Type of hardware for this RFP

    :type hwTypeLocked: bool
    :param hwTypeLocked: Read only value to indicate the possibility to configure the hwType. 
                         Until the RFP did not connect ever to the OMM the value is false 
                         and hwType can be configured. The value never changes from true to false!

    :type wlanProfile: int
    :param wlanProfile: WLAN profile 0 is invalid

    :type wlanAntennaDiv: bool
    :param wlanAntennaDiv: True if WLAN antenna diversity is set

    :type wlanAntenna: int
    :param wlanAntenna: Selected WLAN antenna, 1 or 2

    :type wlanChannel: int
    :param wlanChannel: Configured WLAN channel, one of 1 to 14, 36, 40, 44, 48, 52, 56, 
                        60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 147, 
                        151, 155, 159, 163, 167, 171

    :type wlanHighThroughput: bool
    :param wlanHighThroughput: True if WLAN high throughput mode 40 is set

    :type wlanPower: int
    :param wlanPower: Configured WLAN transmit power in percent, one of 6, 12, 25, 50, 100

    :type conferenceChannels: bool
    :param conferenceChannels: True if this RFP can be used for conference channels

    :type connected: bool
    :param connected: True if this RFP is connected, transient

    :type ipAddr: str
    :param ipAddr: Current or last known IP address, transient

    :type newSoftwareRequest: bool
    :param newSoftwareRequest: True if this RFP requested the OMM to load new software, transient

    :type dectRunning: bool
    :param dectRunning: True if the DECT is running on this RFP, transient

    :type wlanRunning: bool
    :param wlanRunning: True if the WLAN is running on this RFP, transient

    :type ommRunning: bool
    :param ommRunning: True if the OMM is running on this RFP, transient

    :type ommStbRunning: bool
    :param ommStbRunning: True if the standby OMM is running on this RFP, transient

    :type hasWlan: bool
    :param hasWlan: True if WLAN is supported by this RFP hardware, transient

    :type hasEncryption: bool
    :param hasEncryption: True if encryption is supported by this RFP hardware, transient

    :type hasAdvancedFeatures: bool
    :param hasAdvancedFeatures: True if Hi-Q audio technology (wide band) G.722, terminal 
                                video, DECT security and secure SIP are supported by this RFP 
                                hardware, transient

    :type syncState: RFPSyncStateType
    :param syncState: Current DECT synchronization state for this RFP, transient

    :type swVersion: str
    :param swVersion: Current software version on this RFP in the format: 
                      <majorRelease>.<minorRelease>.{RC x | SP y | <bugfixVersion>} 
                      [ Build z] [version description], transient

    :type brandingMismatch: bool
    :param brandingMismatch: True if branding of this RFP and OMM do not fit together, transient

    :type versionMismatch: bool
    :param versionMismatch: True if software version of this RFP and OMM do not fit together, transient

    :type stbMismatch: bool
    :param stbMismatch: True if this RFP has an invalid OMM standby configuration, transient

    :type wlanLinkNok: bool
    :param wlanLinkNok: True if the Ethernet link is too slow (e.g. only 10 MBit/s) 
                        to enable WLAN on this RFP, transient

    :type wlanChannelUsed: int
    :param wlanChannelUsed: Used Channel one of 1 to 14, 36, 40, 44, 48, 52, 56, 60, 64, 100, 
                            104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 147, 151, 155, 
                            159, 163, 167, 171. This value is read only. transient

    :type wlanHighThroughputTypeUsed: str
    :param wlanHighThroughputTypeUsed: Used high throughput channel type, one of “None”, “HT20”, “HT40Minus” or “HT40Plus”. This value is read only. transient

    :type wlanPowerUsed: int
    :param wlanPowerUsed: Used WLAN transmit power in DBM (decibel per milliwatt). transient
                          This value is read only.

    :type nSyncRels: int
    :param nSyncRels: Number of DECT synchronization relations, transient

    :type radioType: RFPRadioTypeType
    :param radioType: The DECT radio type of this RFP

    :type outdoorType: bool
    :param outdoorType: True if this is an outdoor RFP hardware

    :type hasFreqShift: bool
    :param hasFreqShift: True if frequency shift is supported for this RFP
    """
    id = None
    ethAddr = None
    dectOn = None
    wlanOn = None
    licenseRfp = None
    name = None
    hierarchy1 = None
    hierarchy2 = None
    hierarchy3 = None
    hierarchy4 = None
    rpn = None
    pagingArea = None
    cluster = None
    preferredSync = None
    reflectiveEnv = None
    site = None
    x = None
    y = None
    hwType = None
    hwTypeLocked = None
    wlanProfile = None
    wlanAntennaDiv = None
    wlanAntenna = None
    wlanChannel = None
    wlanHighThroughput = None
    wlanPower = None
    conferenceChannels = None
    connected = None
    ipAddr = None
    newSoftwareRequest = None
    dectRunning = None
    wlanRunning = None
    ommRunning = None
    ommStbRunning = None
    hasWlan = None
    hasEncryption = None
    hasAdvancedFeatures = None
    syncState = None
    swVersion = None
    brandingMismatch = None
    versionMismatch = None
    stbMismatch = None
    wlanLinkNok = None
    wlanChannelUsed = None
    wlanHighThroughputTypeUsed = None
    wlanPowerUsed = None
    nSyncRels = None
    radioType = None
    outdoorType = None
    hasFreqShift = None
    _ommclient = None
    _changes = None
    _changelock = Lock()

    def __init__(self, ommclient, attributes=None):
        self.__dict__["_ommclient"] = ommclient
        self.__dict__["_changes"] = {}
        if attributes is not None:
            self._init_from_attributes(attributes)

    def __repr__(self):
        return self.id

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        if key == "hwType" and "hwType" in self.__dict__ and self.__dict__["hwTypeLocked"] == True:
            raise Exception("Cannot change HardwareType!")
        with self._changelock:
            self._changes[key] = value
            self.__dict__[key] = value

    def _init_from_attributes(self, attributes):
        for key, val in list(attributes.items()):
            self.__dict__[key] = val
