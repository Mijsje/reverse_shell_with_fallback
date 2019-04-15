#!/bin/bash

sudo socat file:`tty`,raw,echo=0 tcp-listen:4444
