# ==========================================================
# Exercício 22 - Reprodutor de MP3
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que reproduz um arquivo MP3 utilizando a biblioteca pygame.
# ==========================================================


import pygame
print ('*'*27)
print ('| TOCANDO UM ARQUIVO MP3! |')
print ('*'*27)

pygame.mixer.init()
pygame.mixer.music.load('somex21.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass