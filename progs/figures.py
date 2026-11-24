def find_first_figure_position(phrase):
    coords = phrase[:2]
    x = ord(coords[0])-ord('a')
    y = int(coords[1]) - 1
    return x, y

def find_second_figure_position(phrase):
    coords = phrase[2:]
    x = ord(coords[0])-ord('a')
    y = int(coords[1]) - 1
    return x, y

def find_figure(x, y, figures_on_field):
    i = 0
    while True:
        if figures_on_field[i].x==x and figures_on_field[i].y==y:
            return figures_on_field[i]
        i+=1

def delete_figure_from_table(x, y, field, figures_on_field):
    figure_to_delete = find_figure(x, y, figures_on_field)
    field[figure_to_delete.x][figure_to_delete.y] = '*'
    figures_on_field.remove(figure_to_delete)



class Figure:
    def __init__(self, x, y, color, id_char):
        self.x = x
        self.y = y
        self.color=color
        self.id_char = id_char
    def is_move_correct(self, x_end, y_end, figures_on_field):
        pass
    def make_move(self, move, field, figures_on_field):
        x_end, y_end = find_second_figure_position(move)
        if self.is_move_correct(x_end, y_end, figures_on_field):
            if field[x_end][y_end]!='*':
                figure_in_end = find_figure(x_end, y_end, figures_on_field)
                if figure_in_end.color == self.color: raise Exception("impossible move")
                else:
                    delete_figure_from_table(x_end, y_end, field, figures_on_field)
                    field[x_end][ y_end] = self.id_char
                    field[self.x][self.y] = '*'
                    self.x, self.y = find_second_figure_position(move)
            else: 
                field[self.x][self.y] = '*'
                self.x, self.y = find_second_figure_position(move)
                field[self.x][self.y] = self.id_char
        else: raise Exception("impossible move")

#в целом сюда добавить проверку на то, что ходим не на свою фигуру (и пешечку доработать)
class King(Figure):
    def is_move_correct(self, x_end, y_end, figures_on_field):
        if (abs(x_end-self.x)==1 and self.y==y_end) or (abs(y_end-self.y)==1 and self.x==x_end) or (abs(x_end-self.x)==1 and abs(self.y-y_end)==1):
            return True 
        return False

class Queen(Figure):
    def is_move_correct(self, x_end, y_end, figures_on_field):
        if (self.x==x_end and self.y!=y_end) or (self.y==y_end and self.y!=x_end) or (abs(x_end-self.x)==abs(y_end-self.y)):
            return True 
        return False

class Bishop(Figure):
    def is_move_correct(self, x_end, y_end, figures_on_field):
        if (abs(self.x-x_end)==abs(self.y-y_end)) and (self.x!=x_end): return True 
        return False  

class Knight(Figure): #на теством поле обозначение h-horse
    def is_move_correct(self, x_end, y_end, figures_on_field):
        if (abs(x_end-self.x)==1 and abs(y_end-self.y)==2) or (abs(y_end-self.y)==1 and abs(x_end-self.x==2)): 
            return True
        return False

class Castle(Figure): #ладья вообще-то сейчас rook, но я забуду, кто это
    def is_move_correct(self, x_end, y_end, figures_on_field):
        if (self.x==x_end and self.y!=y_end) or (self.y==y_end and self.x!=x_end):
            return True 
        return False 

class Pawn(Figure): #пешка
    def is_move_correct(self, x_end, y_end, figures_on_table):
        if (self.x==x_end): #добавить съедение
            if self.color=='w':
                if self.y==1 and (y_end-self.y==1 or y_end-self.y==2): return True
                elif self.y!=1 and y_end-self.y==1: return True 
            else:
                if self.y==6 and (y_end-self.y==-2 or y_end-self.y==-1): return True
                elif self.y!=6 and y_end-self.y==-1: return True
        else:
            if self.color=='w':
                if ((y_end-self.y)==1 and abs(x_end-self.x)==1) and find_figure(x_end, y_end, figures_on_table).color=='b': return True 
                return False 
            else:
                if ((y_end-self.y)==-1 and abs(x_end-self.x)==1) and find_figure(x_end, y_end, figures_on_table).color=='w': return True 
                return False
        return False

def GENERAL_make_move(phrase, field, figures_on_field):
    x, y = find_first_figure_position(phrase)
    figure_to_move = find_figure(x, y, figures_on_field)
    figure_to_move.make_move(phrase, field, figures_on_field)

def print_field(field):
    for i in field:
        for j in i:
            print(j, end=' ')
        print()

figures_on_field= []
for i in range(8):
    figures_on_field.append(Pawn(i, 1, 'w', 'p'))
    figures_on_field.append(Pawn(i, 6, 'b', 'p'))
for i in [0, 7]:
    figures_on_field.append(Castle(i, 0, 'w', 'C'))
    figures_on_field.append(Castle(i, 7, 'b', 'C'))
for i in [1, 6]:
    figures_on_field.append(Knight(i, 0, 'w', 'H'))
    figures_on_field.append(Knight(i, 7, 'b', 'H'))
for i in [2, 5]:
    figures_on_field.append(Bishop(i, 0, 'w', 'B'))
    figures_on_field.append(Bishop(i, 7, 'b', 'B'))
figures_on_field.append(King(4, 0, 'w', 'K'))
figures_on_field.append(King(4, 7, 'b', 'K'))
figures_on_field.append(Queen(3, 0, 'w', 'Q'))
figures_on_field.append(Queen(3, 7, 'b', 'Q'))
field = [['*' for i in range(8)] for j in range(8)]
for fig in figures_on_field:
    field[fig.x][fig.y] = fig.id_char
while True:
    print_field(field)
    phrase = input()
    GENERAL_make_move(phrase, field, figures_on_field)
