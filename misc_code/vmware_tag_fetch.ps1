# Connect to vCenter and retrieve VM tags
Import-Module VMware.PowerCLI
Connect-VIServer -Server <VCENTER> -Credential (Get-Credential)
$vmList = Get-VM
$output = @()

foreach ($vm in $vmList) {
    $tags = (Get-TagAssignment -Entity $vm).Tag.Name -join ', '
    $output += [PSCustomObject]@{ VMName = $vm.Name; Tags = $tags }
}
$output | Export-Csv -Path vm_tags.csv -NoTypeInformation