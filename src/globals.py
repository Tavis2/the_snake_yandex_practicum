import pygame
import random
import time

CELL_SIZE = 20

WIDTH, HEIGHT = CELL_SIZE*32, CELL_SIZE*24
LOW_PANELSIZE = CELL_SIZE*6


colors ={
    "background":(0, 0, 0), #чёрный фон
    "lines":(50, 50, 50), #серый линии
    "apple":(230, 20, 20 ), #красный яблоко
    "snake":(20, 230, 20), #зелёный змейка
    "colision":(255, 130, 0) #колизия
}