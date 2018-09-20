#!/bin/sh
echo "muditha"

MAIN_TOUCH=""
CTD_TOUCH=""
MAIN_TOUCH_EVENT=""
CTD_TOUCH_EVENT=""

logger="logger -t touch-monitor -s"
$logger "running Touch monitor tool"

HARDWARE=`/usr/sbin/cincoinfo | sed -n 's/HARDWARE:\([^\s]*\)\s*$/\1/p'`
$logger  "current device is = $HARDWARE"

if [ "$HARDWARE" = "DATAVAN" ] ; then
   $logger "*************************DATAVAN********* Touch device monitoring"
   MAIN_TOUCH=`cat /proc/bus/input/devices | egrep "eGalax Inc. eGalaxTouch EXC7200"  | grep -v "Pen" | cut -d'"' -f 2`
   CTD_TOUCH=`cat /proc/bus/input/devices | egrep "eGalax Inc. eGalaxTouch EXC3000" | grep -v "Pen"| cut -d '"' -f 2`
fi
if [ "$HARDWARE" = "V3" ] ; then
   $logger "*************************V3************** Touch device monitoring"
   MAIN_TOUCH=`cat /proc/bus/input/devices | egrep "eGalax Inc. eGalaxTouch EXC3188"  | grep -v "Pen"| cut -d'"' -f 2`
   CTD_TOUCH=`cat /proc/bus/input/devices | egrep "eGalax Inc. eGalaxTouch EXC3146" | grep -v "Pen"| cut -d'"' -f 2`
fi
if [ "$HARDWARE" = "POINDUS" ] ; then
   $logger "*************************POINDUS********* Touch device monitoring"
   MAIN_TOUCH=`cat /proc/bus/input/devices | egrep "eGalax Inc. eGalaxTouch EXC7200-751Ev1"  | grep -v "Pen"| cut -d'"' -f 2`
   CTD_TOUCH=`cat /proc/bus/input/devices | egrep "eGalax Inc. eGalaxTouch EXC7200-75CCv1" | grep -v "Pen"| cut -d '"' -f 2`
fi

$logger "Device main touch = $MAIN_TOUCH"
$logger "Device ctd touch = $CTD_TOUCH"

if [ -z "$MAIN_TOUCH" ] ; then
   $logger "************************Main touch not detected:- $MAIN_TOUCH"
   exit 2;
else
   MAIN_TOUCH_EVENT=`cat /proc/bus/input/devices | grep -v "Pen" | egrep "$MAIN_TOUCH"  -A4 | egrep -Eo "event([0-9]+[^0-9])"`
   $logger "$MAIN_TOUCH_EVENT"
   (./GetEvent /dev/input/$MAIN_TOUCH_EVENT $HARDWARE) & 
fi 

if [ -z "$CTD_TOUCH" ] ; then
   $logger "************************CTD touch not detected: - $CTD_TOUCH"
   exit 3;
else
   CTD_TOUCH_EVENT=`cat /proc/bus/input/devices | grep -v "Pen" | egrep "$CTD_TOUCH" -A4 | egrep -Eo "event([0-9]+[^0-9])"`
   $logger "$CTD_TOUCH_EVENT"
   (./GetEvent /dev/input/$CTD_TOUCH_EVENT $HARDWARE "CTD") &
fi
 
