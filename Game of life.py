import numpy as np
import pygame
import time

# Set colors 
bg_color = (50, 50, 50)
grid_color = (0, 0, 0)
die_color = (219,112,147)
alive_color = (255, 255, 255)

def update(screen, cells, size, with_progress=False):
    # Set updated cells to a zeros matrix
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        # Find the alive cells by summing the cells in the two adjacent rows and columns and subtracting the cell 
        alive_cells = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = bg_color if cells[row, col] == 0 else alive_color
        
        #Apply rules of the game of life
        # Cell is alive(1)
        if cells[row, col] == 1:
            if alive_cells < 2 or alive_cells > 3:
                if with_progress:
                    color = die_color
            elif 2 <= alive_cells <=3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = alive_color
        # Cell is dead(0)
        else:
            if alive_cells == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = alive_color
        
        # Draw rectangles, using as backgorund the screen value. The sizes of the rectangles are left, top, width, height
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        
    return updated_cells

def main():
    #Initialize pygame
    pygame.init()
    
    #Init surface/screen
    screen = pygame.display.set_mode((800, 600))
    
    # Set dimension of cells
    cells = np.zeros((60, 80))
    
    # Fill the screen with the grid
    screen.fill(grid_color)
    
    # Set size of cells
    size=13
    
    update(screen, cells, size)
    
    #Update the full screen
    pygame.display.flip()
    #Update only portions of the screen
    pygame.display.update()
    
    # Initialize running as false, so it won't immediately start the game
    running = False
    
    # Create infinite while loop to listen to keys 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # If space key is pressed, change running in true/flase
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, size)
                    pygame.display.update()                    
            # Listen to mouse clicks
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                if cells[position[1] // size, position[0]// size] == 0:
                    cells[position[1] // size, position[0]// size] = 1
                else:
                    cells[position[1] // size, position[0]// size] = 0
                update(screen, cells, size)
                pygame.display.update()
    
    
        if running:
            cells = update(screen, cells, size, with_progress=True)
            pygame.display.update()
        time.sleep(0.05)

if __name__ == '__main__':
    main()
    
    
        
    
         