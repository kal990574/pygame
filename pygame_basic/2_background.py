import pygame
pygame.init() #초기화

#화면 크기 설정
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("JaeGu Game") #게임이름  

#배경 이미지 불러오기
background =pygame.image.load("C:\\Users\\kal99\\Desktop\\PythonWorkspace\\pygame_basic\\background.png")
#이벤트 루프
running=True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 ?
            running=False
    #screen.fill((0,0,255))
    screen.blit(background,(0,0))  # 배경 그리기

    pygame.display.update() # 게임 화면을 다시 그리기!

#pygame 종료
pygame.quit()