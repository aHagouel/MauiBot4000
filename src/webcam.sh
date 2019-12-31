#!/bin/bash
file="/home/pi/Development/MauiBot4000/media/img${1}.jpg"
fswebcam -r 1280x720 --no-banner $file -S 20
