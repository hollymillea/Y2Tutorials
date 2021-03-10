import pygame
import random

class GameClass():
    def __init__(self):
        # Grid size
        self.Width = None
        self.Height = None
        self.Scale = None
        # Colours
        self.BackgroundColour = (0,0,0)
        self.TextColour = None
        self.FoodColour = None
        self.SnakeColour = None
        # Other
        self.FoodPosition = None
        self.GameSpeed = None
        self.Score = 0
        # Initialise pygame
        pygame.init()
        self.Display = pygame.display.set_mode( (self.Width * self.Scale, self.Height * self.Scale) )
        self.Clock = None
        pygame.display.set_caption('Snake')


    # MAIN - GAME LOOP
    def Play(self):
        GameOver = False
        while not GameOver:
            self.DisplayFrame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameOver = True
                if event.type == pygame.KEYDOWN:
                    """ if event.key == pygame.K_LEFT:
                    elif event.key == pygame.K_RIGHT:
                    elif event.key == pygame.K_UP:
                    elif event.key == pygame.K_DOWN: """


    def DisplayFrame(self):
        # Reset from the previous frame
        self.Display.fill(self.BackgroundColour)

        # Tell pygame to update its display
        pygame.display.update()

    
    def DisplayText(self,Message,Point):
        # Scale up from our grid system to pixels
        Point = [ x*self.Scale for x in Point ]
        # Set the font and size
        Font = pygame.font.SysFont('dejavusansmono', 25)
        TextSurface = Font.render(Message, True, self.TextColour)
        self.Display.blit(TextSurface, Point)



    # TASK 1
    def ColourCell(self, Position, Colour):
        return

    # TASK 5
    def NewFood(self):
        return




# TASK 2
class SnakeClass():
    def __init__(self):
        self.Head = [0,0]
        self.Body = [self.Head]
        self.PreviousCell = None

    # TASK 3
    def Move(self, Direction):
        return

    # TASK 5
    def EatenFood(self, FoodPosition):
        return

    # TASK 6
    def EatenSelf(self):
        return

    # TASK 6
    def OffScreen(self, Width, Height):
        return



#Snake = GameClass()
#Snake.Play()