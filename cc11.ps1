# Enable File and Printer Sharing

Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

# Allow ICMP Traffic

netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4 

# Enable Remote Management

Enable-PSRemoting -SkipNetworkProfileCheck

# Remove Bloatware

iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

# Enable Hyper-V

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All 

# Disable SMBv1, an insecure protocol

Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol | Disable-WindowsOptionalFeature

# End