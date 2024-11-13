#!/bin/bash

# ras 3+2
((res=3+2))
echo $res

: '
3+2
9
'
((res=4+5))
echo $res