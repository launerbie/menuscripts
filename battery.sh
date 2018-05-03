#!/bin/sh

acstate=`acpi -a | awk -F ' ' '{print $3}'`
percentageleft=`acpi -b | awk -F ', ' '{print $2}'`
timeleft=`acpi -b | cut -d ',' -f 3`

state=`acpi -b | cut -d ':' -f 2 | cut -d ',' -f 1 | tr -d ' '`


if [ "$state" == "Charging" ]
  then
      chargestate="charging"
  else
      chargestate="discharging"
fi

echo [battery $percentageleft, $timeleft]

