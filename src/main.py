from Board import Board
from InputParser import InputParser
from AI import AI
import sys
import random

WHITE = True
BLACK = False

def askForPlayerSide():
    playerChoiceInput = input(
        "What side would you like to play as [w/B]? ").lower()
    if 'w' in playerChoiceInput:
        print("You will play as white")
        return WHITE
    else:
        print("You will play as black")
        return BLACK

AIxAI = 0
PVP   = 1
PVE   = 2

def GameMode():
    print("GameModes:\n\tAi versus ai : 0\n\tPlayer versus player : 1\n\tAi versus ai : 2")
    playerChoiceInput = input("Game mode to be used[0/1/2]?")
    try:
        mode = int(playerChoiceInput)
        if not (mode < 0 or mode > 2):
            return mode
        else:
            raise ValueError('Only value between 0 and 2')
    except ValueError as e:
            print("Incorrect answer:{}".format(str(e)))
            return GameMode()

def askForDepthOfAI():
    depthInput = 2
    try:
        depthInput = int(input("How deep should the AI look for moves?\n"
                               "Warning : values above 3 will be very slow."
                               " [n]? "))
    except:
        print("Invalid input, defaulting to 2")
    return depthInput


def printCommandOptions():
    undoOption = 'u : undo last move'
    printLegalMovesOption = 'l : show all legal moves'
    randomMoveOption = 'r : make a random move'
    quitOption = 'quit : resign'
    moveOption = 'a3, Nc3, Qxa2, etc : make the move'
    options = [undoOption, printLegalMovesOption, randomMoveOption,
               quitOption, moveOption, '', ]
    print('\n'.join(options))


def printAllLegalMoves(board, parser):
    for move in parser.getLegalMovesWithShortNotation(board.currentSide):
        print(move.notation)


def getRandomMove(board, parser):
    legalMoves = board.getAllMovesLegal(board.currentSide)
    randomMove = random.choice(legalMoves)
    randomMove.notation = parser.notationForMove(randomMove)
    return randomMove


def makeMove(move, board):
    print()
    print("Making move : " + move.notation)
    board.makeMove(move)


def printPointAdvantage(board):
    print("Currently, the point difference is : " +
          str(board.getPointAdvantageOfSide(board.currentSide)))


def undoLastTwoMoves(board):
    if len(board.history) >= 2:
        board.undoLastMove()
        board.undoLastMove()


def startGameAi(board, playerSide, ai):
    parser = InputParser(board, playerSide)
    while True:
        print(board)
        print()
        if board.isCheckmate():
            if board.currentSide == playerSide:
                print("Checkmate, you lost")
            else:
                print("Checkmate! You won!")
            return

        if board.isStalemate():
            if board.currentSide == playerSide:
                print("Stalemate")
            else:
                print("Stalemate")
            return

        if board.currentSide == playerSide:
            # printPointAdvantage(board)
            move = None
            command = input("It's your move."
                            " Type '?' for options. ? ").lower()
            if command == 'u':
                undoLastTwoMoves(board)
                continue
            elif command == '?':
                printCommandOptions()
                continue
            elif command == 'l':
                printAllLegalMoves(board, parser)
                continue
            elif command == 'r':
                move = getRandomMove(board, parser)
            elif command == 'quit':
                return
            else:
                move = parser.moveForShortNotation(command)
            if move:
                makeMove(move, board)
            else:
                print("Couldn't parse input, enter a valid command or move.")

        else:
            print("AI thinking...")
            move = ai.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)


def startGameAIxAI(board, aiWhite, aiBlack):
    parser = InputParser(board, playerSide)
    while True:
        print(board)
        print()
        if board.isCheckmate():
            if board.currentSide == WHITE:
                print("Checkmate, White AI wins!")
            else:
                print("Checkmate! Black AI wins!")
            return

        if board.isStalemate():
                print("Stalemate")

        if board.currentSide == WHITE:
            print("White AI thinking...")
            move = aiWhite.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)

        else:
            print("Black AI thinking...")
            move = aiBlack.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)

def startGameX1(board):
    white_turn = True;
    parser = InputParser(board, WHITE)
    while True:
        print(board)
        print()
        if board.isCheckmate():
            if board.currentSide == WHITE:
                print("Checkmate, WHITE win!")
            else:
                print("Checkmate! BLACK win!")
            return

        if board.isStalemate():
                print("Stalemate")

        move = None
        command = None
        changeColor = False
        if board.currentSide == WHITE:
            command = input("WHITE:"
                            " Type '?' for options. ? ").lower()
        else:
            command = input("BLACK:"
                            " Type '?' for options. ? ").lower()
            
        # printPointAdvantage(board)

        print("command: {}".format(command))
       
        if command == 'u':
            undoLastTwoMoves(board)
            continue
        elif command == '?':
            printCommandOptions()
            continue
        elif command == 'l':
            printAllLegalMoves(board, parser)
            continue
        elif command == 'r':
            move = getRandomMove(board, parser)
        elif command == 'quit':
            return
        else:
            move = parser.moveForShortNotation(command)

        if move:
            changeColor = True
            print("MOVE")
            board.makeMove(move)
        else:
            print("Couldn't parse input, enter a valid command or move.")

board = Board()
playerSide = WHITE
GM = GameMode()
print()

try:
    if(GM != PVP)
        aiDepth = askForDepthOfAI()
    

    if GM == PVP:
        startGameX1(board)
    elif GM == AIxAI:
        WHITEai = AI(board, WHITE, aiDepth)
        BLACKai = AI(board, BLACK, aiDepth)

        startGameAIxAI(board, WHITEai, BLACKai)
    else:
        opponentAI = AI(board, not playerSide, aiDepth)
        startGameAi(board, playerSide, opponentAI)

except KeyboardInterrupt:
    sys.exit()
