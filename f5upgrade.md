# F5 VE Upgrade steps

- Download the required F5 VE version from https://downloads.f5.com/
- Get the OVA version for the vmware host
- Load the OVA imageset to ESXi host
    - Assign the VLANs as like in current SoftLayer F5s.
- Configure the temporary management IP address
- Follow the steps from K7752 to activate F5 license
   - Activating the license using the manual activation method
    ***Impact of procedure***: Traffic processing is briefly interrupted while the BIG-IP system reloads the configuration. When licensing redundant BIG-IP systems, F5 recommends that you activate the license on your BIG-IP devices while they are in standby mode.
        1. Log in to the Configuration utility.
            ***Note***: If this is a new BIG-IP system, open a web browser on a workstation attached to the network on which you configured the management port and type the following URL in the browser: https://<IP address>/. <IP_address> is the address that you configured for the management port.
        2. Select Activate.
            > Note: If the BIG-IP system is already licensed, navigate to System > License and select Re-activate. Optionally on BIG-IP 12.1.0 and later, select the Enable License Comparison check box to compare a new license with the existing BIG-IP license.

        3. Select Manual.
        4. Select Next.
        5. Copy the dossier and connect to the F5 Product Licensing page at secure.f5.com.
        6. On the F5 Licensing Tools page, select Activate F5 product registration key for BIG-IP 9.x and later.
        7. Paste the dossier into the Enter Your Dossier box, and then select Next.
        The F5 Product Licensing page produces your license.
        8. Copy the license and paste it into the License box in the Configuration utility.
        9. Select Next.
            > **Important:** Traffic processing is briefly interrupted while the BIG-IP system reloads the configuration.

- Backup the F5 device (Standby) that is being upgraded 
    > Follow the steps from K1312 for backing up and restoring F5 configuration files with a UCS archive

    If there any encrypted password issues like below. 
    *`0107102b:3: Master Key decrypt failure - decrypt failure - final`*
    > Follow Steps from K9420 for files containing encrypted passwords or passphrases

- On upgrade window follow the below steps to take-out an F5 and bring-in new F5
    - Take the baseline validation
        - take notes, screenshots and counts of current F5 object statuses (active/green,red,blue etc)
    - Force offline a device to be upgraded (`Standby`)
    - Poweroff the `Standby` device which is forced offline and use the Mgmt IP address from it to new device
        > Make sure the configration backup is taken before poweroff.
    
    - Restore the configuration from the backup from `Standby` device
    - After the successful restore verify the F5 objects
    - If everything is as expected then, bring Active device offline and bring up new device active to validate.
    - Perform the validation against the baseline.
    - Release it for functional validation.
