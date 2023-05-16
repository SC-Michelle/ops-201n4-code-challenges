# Ops Challenge 12

function IP {
    ipconfig /all | Out-File -FilePath $file
}
$file= "C:\Users\Admin\Documents\network_report.txt"
IP
Select-String -Path $file -Pattern IPv4
Remove-Item -Path $file

# End