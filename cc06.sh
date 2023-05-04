x=1
FILE="test.txt"
 while [ $x = 1 ]

do
if [ -f "$FILE" ]
then
   echo "File $FILE exist."
else
    echo "File $FILE does not exist" 
     touch $FILE
fi 

echo "press 1 to run again"
read x
done
