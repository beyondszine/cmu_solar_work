#!/bin/bash

device=/dev/video0
path_to_upload=/cmu_work/
streamer -c $device -o output.jpeg
sleep 1
if [ $? == '0' ]
then
	echo "pic clicked successfully"
	/home/pi/cmu_solar_work/progs/dropbox_uploader.sh upload output.jpeg $path_to_upload
fi
