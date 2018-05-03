#!/bin/sh

acstate=`acpi -a | awk -F ' ' '{print $3}'`
left=`acpi -b | awk -F ', ' '{print $2}'`

state=`acpi -b | cut -d ':' -f 2 | cut -d ',' -f 1 | tr -d ' '`

if [ "$state" == "Charging" ]
  then
      chargestate="charging"
  else
      chargestate="discharging"
fi

echo [AC $acstate] [battery $left $chargestate]

