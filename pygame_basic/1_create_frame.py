import pygame
pygame.init() #초기화
#화면 크기 설정
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("JaeGu Game") #게임이름

#이벤트 루프
running=True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 ?
            running=False

#pygame 종료
pygame.quit()