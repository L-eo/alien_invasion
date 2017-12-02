# -*- coding:utf-8 -*-
import pygame

def bg_image_load():
    """循环主体之前加载图像"""

    # 对于所需要的背景图命名，将背景图片加载和转化
    image1_filename = 'images/bgimg1.png'
    image2_filename = 'images/bgimg2.png'
    bgimage1 = pygame.image.load(image1_filename).convert()
    bgimage2 = pygame.image.load(image2_filename).convert()

    # 生成一个image列表，后面将列表所有元素的同时向前移动
    bgimage = [bgimage1, bgimage2]
    return bgimage
    

def bg_image_roll(ai_settings, screen, bgimage, bg_position):
    """循环主体之中，背景图持续滚动"""
    bg_position[1] += ai_settings.alien_speed #通过改变数值能够改变滑动的速度
    bgimage1, bgimage2 = bgimage
    if bg_position[1] >= 620:  # 图片垂直滑动的算法
        bgimage = bgimage[1:]+bgimage[:1]
        # 每当列表中的第一张图片左移动至完全消失的时候，将第一张图片加到列表的末尾
        bgimage1, bgimage2 = bgimage
        bg_position[1] = 0
    
    # 把背景图依次画到屏幕上
    screen.blit(bgimage1, (bg_position[0], bg_position[1]))
    screen.blit(bgimage2, (bg_position[0], bg_position[1]-600))