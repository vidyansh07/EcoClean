# Car-Bon Monox

## Differences b/w two implementations :

|No. | Old Implementation | New Implementation|
|-|-|-|
|1.| Old System used to send just sms to inform the user of increase in CO Gas | Information to user is now sent via SMS , Phone call as well as App Notification in the new system |
|2.| Old System used Old Technologies like DTMF and GPRS to initiate sending of SMS | New system is using newer technologies like VOIP SMS and Calls with preset message including current status to inform the user |
|3.| Old System had its fair share of problems due to the old technology being in use like network issue due to network type being GPRS | New system uses cloud based information sending , therefore there is a lesser chance of hardware limitations|
|4.| Old system only measured CO values and lowered the window | New system measures not only CO but Temprature and humidy as well as network based location |
|5.| Old system did not collect any data for analysis | New system collects data for analysis, which can be further led into a machine learning model to predict and prevent future occurences |
|6.| Old system did not provide an interface for user to see historical data and check for health of system / vehicle | New System comprises of a UI dashboard along with mobile application to monitor the health of system and vehilce along with visibility over any historical data.| 
|7.| Old system used old hardware with less capable microcontorller based on Arduino | New System uses a better smaller and more capable microcontroller based on ESP32. Moreover the newer system has another variant which can act as an individal device able to show stats on the device itself along woth showing on a dashboard.|