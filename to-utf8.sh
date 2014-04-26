## Procedure to convert all the files from:
##    TXT with ISO-8891-1 encoding --> CSV with UTF-8 encoding
for x in $@;do
  newfile=$(echo $x | sed 's/TR_EXP_\(.*\).TXT/\L\1.csv/')
  if [ -n $quiet ]; then
     echo "Converting file $x (ISO-8859-1) to $newfile (UTF-8)"
  fi
  iconv --verbose --from-code=ISO-8859-1 --to-code=UTF-8 $x > $newfile
done
