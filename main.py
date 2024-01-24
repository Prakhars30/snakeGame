import pygame,sys,asyncio
import random

Apple_pos = [100,100]
Head_pos = [0,20]
Snake_pos = [[0,0]]
Snake_length = [1]

class Snake:
    def __init__(self,s):
        pygame.draw.rect(s,("Red"),pygame.Rect(Apple_pos[0],Apple_pos[1],20,20),0,10)
        pygame.draw.rect(s,("Green"),pygame.Rect(Head_pos[0],Head_pos[1],20,20),0,5)
        for i in range(Snake_length[0]):
            pygame.draw.rect(s,("Green"),pygame.Rect(Snake_pos[i][0],Snake_pos[i][1],20,20),5,6)


class Change:
    def __init__(self,key):
        if Head_pos == Apple_pos:
            Snake_length[0] += 1
            while(Apple_pos in Snake_pos or Apple_pos == Head_pos):
                x = random.randrange(0,19)
                y = random.randrange(0,19)
                Apple_pos[0] = x*20
                Apple_pos[1] = y*20
        else:
            Snake_pos.pop(0)


        if key == "right":
            Snake_pos.append([Head_pos[0],Head_pos[1]])
            Head_pos[0] += 20
        if key == "left":
            Snake_pos.append([Head_pos[0],Head_pos[1]])
            Head_pos[0] -= 20
        if key == "up":
            Snake_pos.append([Head_pos[0],Head_pos[1]])
            Head_pos[1] -= 20
        if key == "down":
            Snake_pos.append([Head_pos[0],Head_pos[1]])
            Head_pos[1] += 20

        # if Head_pos[0] < 0:
        #     Head_pos[0] = 380
        # if Head_pos[0] > 381:
        #     Head_pos[0] = 0
        # if Head_pos[1] < 0:
        #     Head_pos[1] = 380
        # if Head_pos[1] > 381:
        #     Head_pos[1] = 0

    def collision(self):
        if Head_pos in Snake_pos:
            return True
        elif Head_pos[0] < 0 or Head_pos[0] > 381 or Head_pos[1] < 0 or Head_pos[1] > 381:
            return True
        else:
            return False

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

    async def main(self):
        Select_key = "right"
        fff = pygame.font.Font(None,20)
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if Select_key != "up":
                            Select_key = "down"
                    elif event.key == pygame.K_UP:
                        if Select_key != "down":
                            Select_key = "up"
                    elif event.key == pygame.K_RIGHT:
                        if Select_key != "left":
                            Select_key = "right"
                    elif event.key == pygame.K_LEFT:
                        if Select_key != "right":
                            Select_key = "left"

            score = "score :" +" "+ str(Snake_length[0])
            ttt = fff.render(score,True,("White"))
            txtx = ttt.get_rect()
            txtx.center = (200,7)

            self.screen.fill('Black')
            self.screen.blit(ttt,txtx)
            Changes = Change(Select_key)
            if(Changes.collision()):
                break
            else:
                Snake(self.screen)
            pygame.display.update()
            self.clock.tick(5)

        fff = pygame.font.SysFont("Monospace",30,True)
        ttt = fff.render('GAME OVER',True,("White"))
        txtx = ttt.get_rect()
        txtx.center = (200,180)

        fff1 = pygame.font.SysFont("Monospace",30,True)
        score = "Your score :" +" "+ str(Snake_length[0])
        ttt1 = fff1.render(score,True,("White"))
        txtx1 = ttt1.get_rect()
        txtx1.center = (200,220)

        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('Black')
            self.screen.blit(ttt,txtx)
            self.screen.blit(ttt1,txtx1)
            pygame.display.update()
            await asyncio.sleep(0)


if __name__ == '__main__':
    game = Game()
    asyncio.run(game.main())