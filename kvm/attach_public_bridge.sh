#!/bin/bash

LANG=C
export LANG

attach_public_bridge()
{
	bridge=virbr0
	if=eth0
	
	brctl show | grep -q $bridge && return
	brctl addbr $bridge
	ipaddr=$(ip addr show $if | awk '/inet / { print $2 }')
	route=$(ip route show | awk '/default via / { print $3 }')
	ip addr del $ipaddr dev eth0
	ip addr flush dev $if
	ip link set $if up
	brctl addif $bridge $if
	ip addr add $ipaddr broadcast + dev $bridge
	ip link set $bridge up
	r=$(ip route show | awk '/default via / { print $3 }')

	if [ -n "$route" -a -z "$r" ]
	then
	ip route add default via $route
	fi
}
attach_public_bridge
