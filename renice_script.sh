#!/bin/bash

# add to /etc/sysctl.conf
# kernel.sched_autogroup_enabled = 0
# load the change: sysctl -p  /etc/sysctl.conf
# check: cat /proc/sys/kernel/sched_autogroup_enabled
# and reset manually: echo 0 > /proc/sys/kernel/sched_autogroup_enabled
# use /etc/sysctl.conf from above
# or add "noautogroup" to the kernel cmdline

arr=("polkitd" "microsoft" "home1" "auditd")

for i in "${!arr[@]}"; do
  for p in $(pgrep -f ${arr[$i]}); do
    # process itself
    sudo renice +19 -p $p
    # child processes
    for c in $(pgrep -P $p); do
      sudo renice +19 -p $p
    done
  done
  # all threads
  for p in $(pgrep -f -w ${arr[$i]}); do
    sudo renice +19 -p $p
  done
done
