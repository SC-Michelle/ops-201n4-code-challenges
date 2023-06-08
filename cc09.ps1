# Task 1

$Begin = Get-Date -Date '5/9/2023 00:00:00'
$End = Get-Date -Date '5/9/2023 23:59:59'

Get-EventLog -LogName System -EntryType Error -After $Begin -Before $End >C:\Users\michelle\Documents\last_24.txt

# Task 2
Get-EventLog -LogName System -EntryType Error >C:\Users\michelle\Documents\error.txt

# Task 3
Get-EventLog -LogName System -InstanceID 16 >C:\Users\michelle\Documents\Task03.txt

# Task 4
Get-EventLog -LogName -Newest 20 >>C:\Users\michelle\Documents\Task04.txt

# Task 5
$Events = Get-EventLog -LogName System -Newest 500
$Events / Group-Object -Property Source -NoElement / Sort-Object -Property Count -Descending >C:\Users\michelle\Documents\Task05.txt