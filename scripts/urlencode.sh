#! /bin/sh

nkf -WwMQ | sed "s/=$//g" | tr -d "\n" | tr "=" "%"
