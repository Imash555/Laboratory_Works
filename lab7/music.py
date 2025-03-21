import pygame
import os

pygame.init()
pygame.mixer.init()

# Load background image
background = pygame.image.load("images/image for music .jpeg")
WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MUSIC_FOLDER = "music"
songs = [song for song in os.listdir(MUSIC_FOLDER) if song.endswith(".mp3")]

if not songs:
    print("No music files found!")
    exit()

current_index = 0
paused = False

# Load and play first song
pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
pygame.mixer.music.play()

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.play()

def stop_music():
    global paused
    pygame.mixer.music.stop()
    paused = True

def next_track():
    global current_index, paused
    current_index = (current_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
    pygame.mixer.music.play()
    paused = False

def previous_track():
    global current_index, paused
    current_index = (current_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
    pygame.mixer.music.play()
    paused = False

run = True
while run:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_music()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
            elif event.key == pygame.K_q:
                stop_music()
                run = False

pygame.quit()

