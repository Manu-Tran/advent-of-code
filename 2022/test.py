#!/usr/bin/env python3

from pythonping import ping
import time
from datadog import initialize, statsd

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

while True:
    a = (ping("192.168.1.254", count=1))
    statsd.gauge('freebox.latency.bazelgeuse.ms', a.rtt_max_ms, tags=["service:bazelgeuse"])
    time.sleep(1)
