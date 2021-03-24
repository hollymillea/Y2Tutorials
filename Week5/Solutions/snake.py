import pygame
import random

class GameClass():
    def __init__(self):
        # Grid size
        self.Width = 30
        self.Height = 20
        self.Scale = 30
        # Colours
        self.BackgroundColour = (0,0,0)
        self.TextColour = (255,255,255)
        self.FoodColour = (255,0,0)
        self.SnakeColour = (0,255,0)
        # Other
        self.FoodPosition = None
        self.GameSpeed = 15
        self.Score = 0
        # Initialise pygame
        pygame.init()
        self.Display = pygame.display.set_mode( (self.Width * self.Scale, self.Height * self.Scale) )
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption('Snake')


    def Play(self):
        # TASK 2
        StartPosition = [self.Width//2, self.Height//2]
        Snake = SnakeClass(StartPosition)
        # TASK 5
        self.NewFood()

        GameOver = False
        # TASK 4
        GameStarted = False
        while not GameOver:
            # TASK 7
            Text = "Score: " + str(self.Score)
            self.DisplayFrame(Snake, Text)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameOver = True
                # TASK 3
                if event.type == pygame.KEYDOWN:
                    # TASK 4
                    GameStarted = True
                    if event.key == pygame.K_LEFT:
                        Direction = "Left"
                    elif event.key == pygame.K_RIGHT:
                        Direction = "Right"
                    elif event.key == pygame.K_UP:
                        Direction = "Up"
                    elif event.key == pygame.K_DOWN:
                        Direction = "Down"
                    # TASK 3
                    #Snake.Move(Direction)
            
            # TASK 4
            if GameStarted:
                Snake.Move(Direction)
            self.Clock.tick(self.GameSpeed)

            # TASK 5
            if Snake.EatenFood(self.FoodPosition):
                self.NewFood()
                Snake.Body.append(Snake.Previous)
                self.Score += 1

            # TASK 6
            if Snake.OffScreen(self.Width,self.Height) or Snake.EatenSelf():
                GamePaused = True
                # TASK 7
                Text = "Score: " + str(self.Score) + ". Please press any key to restart."
                while GamePaused:
                    self.DisplayFrame(Snake,Text)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            GamePaused = False
                            GameOver = True
                        if event.type == pygame.KEYDOWN:
                            NewGame = GameClass()
                            NewGame.Play()
                            return


    def DisplayFrame(self, Snake, Text):
        # Reset from the previous frame
        self.Display.fill(self.BackgroundColour)

        # TASK 1
        #self.ColourCell([1,4],(0,255,0))

        # TASK 2
        for Pixel in Snake.Body:
            self.ColourCell(Pixel,self.SnakeColour)

        # TASK 7
        self.DisplayText(Text, [0,0])

        # TASK 4 - display food
        self.ColourCell(self.FoodPosition, self.FoodColour)

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
        # Scale up the coordinates so we get the true pixel coordinates on our screen
        X,Y = Position
        X = X * self.Scale
        Y = Y * self.Scale
        # Draw a rectangle covering all the screen pixels for our 'cell'
        pygame.draw.rect(
            self.Display,
            Colour,
            [X, Y, self.Scale, self.Scale])

    # TASK 5
    def NewFood(self):
        # X is across so we look at width
        X = random.randint(0,self.Width-1)
        # Y is the vertical axis so we look at height
        Y = random.randint(0,self.Height-1)
        self.FoodPosition = [X,Y]




# TASK 2
class SnakeClass():
    def __init__(self, StartPosition):
        self.Head = StartPosition
        self.Body = [self.Head]
        self.PreviousCell = None

    # TASK 3
    def Move(self, Direction):
        # Making copies to work with instead
        Head = self.Head.copy()
        Body = self.Body.copy()
        
        # Moving the position of the head
        if Direction == "Left":
            # Move the x-coordinate
            Head[0] += -1
        if Direction == "Right":
            # Move the x-coordinate
            Head[0] += 1
        if Direction == "Up":
            # Move the y-coordinate
            Head[1] += -1
        if Direction == "Down":
            # Move the y-coordinate
            Head[1] += 1

        # Save the last block position for later
        self.Previous = Body[-1]

        # Delete the last element from our body
        n = len(Body)
        Body = Body[0:n-1]

        # Add the head to the front of the body
        Body = [Head] + Body
        
        # Update the properties
        self.Body = Body
        self.Head = Head

    # TASK 5
    def EatenFood(self, FoodPosition):
        if self.Head == FoodPosition:
            return True
        else:
            return False

    # TASK 6
    def EatenSelf(self):
        if self.Head in self.Body[1:None]:
            return True
        else:
            return False

    # TASK 6
    def OffScreen(self, Width, Height):
        # Checking the X axis
        X = self.Head[0]
        if (X < 0) or (X >= Width - 1):
            return True
        # Checking Y axis
        Y = self.Head[1]
        if (Y < 0) or (Y >= Height - 1):
            return True
        return False


Snake = GameClass()
Snake.Play()