# Set the O365 admin 'username@contoso.com' here,
# so that none of the code below needs to be modified.
$newAdmin = ""


<# This function adds a user to the local administrators group of a workstation. Assuming that the device is joined to Azure Ad,
   you will be able to add username@contoso.com which will be shown as AzureAD\username within the local administrators group.
   Advantages of using this instead of creating a local admin account, is due to the centralized control of credentials. It will
   also require the credentials to be domain specific.
#>
function Add-LocalAdminAccount {
    param (
        [string[]]$AccountUsername
    )
    Add-LocalGroupMember -Group "Administrators" -Member $AccountUsername
}

<#  Use this function to securely disable the local accounts that are by default on a Windows workstation.
    There is typically no need to have these accounts enabled for security concerns and therefore
    should be disabled. 
#>
function Disable-DefaultLocalUserAccounts {
    $DefaultAccounts = "Administrator", "DefaultAccount", "Guest", "WDAGUtilityAccount"
    foreach ($Account in $DefaultAccounts) {
        Get-LocalUser $Account | Disable-LocalUser
    }
}

<#  Use this function to check for any local accounts that have been added to the workstation. If a value exists outside of this list, then remove it. #>
function Remove-NonDefaultLocalAccounts {
    $SkippedAccount = "Administrator", "DefaultAccount", "Guest", "WDAGUtilityAccount", "defaultuser0", "defaultuser1"
    Get-LocalUser | Where-Object {$SkippedAccount -notcontains $_.Name} | Remove-LocalUser
}

Disable-DefaultLocalUserAccounts
Remove-NonDefaultLocalAccounts
Add-LocalAdminAccount -AccountUsername $newAdmin