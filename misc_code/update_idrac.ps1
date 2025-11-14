# Update these variables for your environment
#Create a local file "server.txt" listing the iDrac IP's
$iDRACUser = "root"
$iDRACPass = "password"
$BIOSFile = "BIOS_X.Y.Z.DUP.exe" # Name of the BIOS update file
$NetworkShare = "//192.168.1.50/Updates" # UNC path to your share

# Read the list of iDRAC IPs
$iDRACs = Get-Content -Path "C:\path\to\servers.txt"

foreach ($iDRAC in $iDRACs) {
    Write-Host "--- Updating BIOS on iDRAC: $iDRAC ---"
    
    # Execute the remote racadm command to start the update
    # The --reboot flag tells the server to reboot automatically after the update is staged
    # It is a good practice to test without --reboot and handle restarts separately
    try {
        racadm.exe -r $iDRAC -u $iDRACUser -p $iDRACPass update -f $BIOSFile -l $NetworkShare --reboot
        Write-Host "Update job submitted for $iDRAC. Check the iDRAC job queue for status."
    }
    catch {
        Write-Host "ERROR: Failed to submit update job for $iDRAC. $($_.Exception.Message)"
    }
}