#!/bin/sh

iwconfig wlp12s0 2>&1 | grep -q no\ wireless\ extensions\. && {
  echo wired
  exit 0
}

essid=`iwconfig wlp12s0 | awk -F '"' '/ESSID/ {print $2}'`
stngth=`iwconfig wlp12s0 | awk -F '=' '/Quality/ {print $2}' | cut -d '/' -f 1`
bars=`expr $stngth / 7`

case $bars in
  0)  bar='[----------]' ;;
  1)  bar='[|---------]' ;;
  2)  bar='[||--------]' ;;
  3)  bar='[|||-------]' ;;
  4)  bar='[||||------]' ;;
  5)  bar='[|||||-----]' ;;
  6)  bar='[||||||----]' ;;
  7)  bar='[|||||||---]' ;;
  8)  bar='[||||||||--]' ;;
  9)  bar='[|||||||||-]' ;;
  10) bar='[||||||||||]' ;;
  *)  bar='[----!!----]' ;;
esac

echo ESSID: $essid $bar

exit 0
