import pygame
import random

CELL_SIZE = 30

WIDTH, HEIGHT = CELL_SIZE*26, CELL_SIZE*20
LOW_PANELSIZE = CELL_SIZE*6


colors ={
    "background":(0, 0, 0), #чёрный фон
    "lines":(50, 50, 50), #серый линии
    "apple":(230, 20, 20 ), #красный яблоко
    "snake":(20, 230, 20), #зелёный змейка
}