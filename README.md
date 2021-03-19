# F5 Utils

I am planning to add series of handy utlity scripts for managing F5 devices. These are intented to run from terminal window. the python scripts can run in windows command-line or mac terminal as long as python is installed on the system.

## F5 HA Pair devices Synchronization Statuses
This script will enumerate through the list of given management-IPs/host names of the devices and gathers sync state, and version information in an csv output. The out may be viewed in Excel. The below is the usage for running script:

`usage: get_devices_sync_state.py -u user_id -f devices.lst`

For example
`python get_devices_sync_state.py -u guru -f my_f5s.txt`

This generated output.csv file and here is the sample output view from Microsoft Excel:

![sample output](sample_output.png)

