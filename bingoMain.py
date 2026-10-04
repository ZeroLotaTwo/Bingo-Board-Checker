from BingoBoardClass import BingoBoard
from BingoBoardWin import BingoBoardWin
from bingoNumCaller import numCaller
import pygame
import sys

board: BingoBoard = BingoBoard()
winTest: BingoBoardWin = BingoBoardWin(board)
dealer: numCaller = numCaller()

window_width = 1920
window_height = 1080
window_title = "FUCKING BINGO!!!!"
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
tileHeight = window_height // board.height
tileWidth = window_width // board.width
font_size = 100
# font = pygame.font.Font(None, font_size)  # None uses the default font

def get_user_number(event, user_input):
    """
    Handles user input to construct a number string based on key events.

    Parameters:
    - event: The Pygame event to process.
    - user_input: The current string representing the user's input.

    Returns:
    - Updated user_input string.
    - Finalized number if the user presses Enter, otherwise None.
    """
    if event.type == pygame.KEYDOWN:
        # print("worked")
        if event.key == pygame.K_BACKSPACE:  # Remove last character
            user_input = user_input[:-1]
        elif event.key == pygame.K_RETURN:  # Submit the number
            try:
                return "", int(user_input)  # Clear input and return the number
            except ValueError:
                return "", None  # Invalid input clears the field
        else:
            # Append valid input (digits or single decimal point)
            if event.unicode.isdigit() or (event.unicode == "." and "." not in user_input):
                user_input += event.unicode
    return user_input, None

def drawBingo(font) -> None:
    for row in range(len(board.getBingoCard())):
        for col in range(len((board.getBingoCard())[row])):
            num = board.getBingoCard()[row][col]
            if num == 0:
                num = "free"
            if(num == "free" or num < 0):
                text_surface = font.render("X", True, (255,0,0))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (tileWidth * col + 140, tileHeight * row + 80) 
                screen.blit(text_surface, text_rect)
            if num != "free":
                num = abs(num)
            text_surface = font.render(str(num), True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (tileWidth * col + 140, tileHeight * row + 80) 
            screen.blit(text_surface, text_rect)
    
def copyBoard():
    global board
    print("please input your numbers from left to right")
    nums = input()
    nums = nums.split()
    #1 2 3 4 5 6 7 8 9 10 11 12 0 13 14 99 88 77 66 55 98 87 76 65 54
    for i in range(board.height):
        for j in range(board.width):
            board.bingoCard[i][j] = int(nums[j + i * board.height])
# Main game loop for demonstration
def main():
    # Initialize Pygame
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Enter a Number")

    # Colors and Font
    white = (255, 255, 255)
    black = (0, 0, 0)
    font = pygame.font.Font(None, 50)

    # User input
    user_input = ""
    user_number = None

    # Main loop
    running = True
    win = 0
    ignoreList = []
    condition = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Process numeric input
            user_input, user_number = get_user_number(event, user_input)

            # Break the loop if the user presses Enter with a valid number
            # if user_number is not None:
            #     print(f"You entered: {user_number}")
            #     running = False

        # Clear screen
        screen.fill(white)

        #Render user input
        prompt = font.render("NUM: ", True, black)
        input_surface = font.render(user_input, True, black)
        screen.blit(prompt, (0, 0))
        screen.blit(input_surface, (100, 0))



        # Update the display
        drawBingo(font)
        if win:
            prompt = font.render(f"{len(condition) - len(ignoreList)} BINGO", True, (0,255,0))
            screen.blit(prompt, (150, 0))
            prompt = font.render("Want to keep playing or clear board? KeepPlaying = 0, Clear Board = 1?", True, (0,0,0))
            screen.blit(prompt, (350, 0))
        if(user_number != None):
            if user_number == 999:
                copyBoard()
            print(ignoreList)
            board.markNum(user_number)
            for idx in range(len(ignoreList) - 1, -1,-1):
                if user_number != 0 and user_number in ignoreList[idx]:
                    del ignoreList[idx]
            if not(win):
                user_number = None
            condition = winTest.normalWin()
            if condition != None:
                for eachWin in condition:
                    if not(eachWin in ignoreList):
                        win = 1 
            if win:
                if user_number == 1:
                    board.clearBoard()
                    ignoreList.clear()
                    win = 0
                    user_number = None
                elif user_number == 0:
                    if condition != None:
                        for eachWin in condition:
                            if(not(eachWin in ignoreList)):
                                ignoreList.append(eachWin)
                    win = 0
                    print(ignoreList)
            # else:
            #     board.markNum(user_number)
            #     user_number = None

        pygame.display.flip()

    pygame.quit()

# if __name__ == "__main__":
main()
