#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyscratch import *

ball = Ball()
while True:
    ball.move(10)
    ball.bounce_if_on_edge()

start()

# 小球游戏
