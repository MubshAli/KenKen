import check
import copy   #needed to copy a nested list to avoid mutating the consumed lists

class Puzzle:
    '''
      Fields:
            size: Nat 
            board: (listof (listof (anyof Str Nat Guess))
            constraints: (listof (list Str Nat (anyof '+' '-' '*' '/' '='))))
    requires: See Assignment Specifications
    '''
    
    def __init__(self, size, board, constraints):
        self.size=size
        self.board=board
        self.constraints=constraints
        
    def __eq__(self, other):
        return (isinstance(other,Puzzle)) and \
            self.size==other.size and \
            self.board == other.board and \
            self.constraints == other.constraints
    
    def __repr__(self):
        s='Puzzle(\nSize='+str(self.size)+'\n'+"Board:\n"
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.board[i][j],Guess):
                    s=s+str(self.board[i][j])+' '
                else:
                    s=s+str(self.board[i][j])+' '*12
            s=s+'\n'
        s=s+"Constraints:\n"
        for i in range(len(self.constraints)):
            s=s+'[ '+ self.constraints[i][0] + '  ' + \
                str(self.constraints[i][1]) + '  ' + self.constraints[i][2]+ \
                ' ]'+'\n'
        s=s+')'
        return s
    

class Guess:
    '''
    Fields:
            symbol: Str 
            number: Nat
    requires: See Assignment Specifications
    '''    
   
    def __init__(self, symbol, number):
        self.symbol=symbol
        self.number=number
        
    def __repr__(self):
        return "Guess('{0}',{1})".format(self.symbol, self.number)
    
    def __eq__(self, other):
        return (isinstance(other, Guess)) and \
            self.symbol==other.symbol and \
            self.number == other.number        

class Posn:
    '''
    Fields:
            x: Nat 
            y: Nat
    requires: See Assignment Specifications
    '''    
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "Posn({0},{1})".format(self.x, self.y)
    
    def __eq__(self,other):
        return (isinstance(other, Posn)) and \
            self.x==other.x and \
            self.y == other.y 

#useful constants for testing
puzzle1 = Puzzle(4, [['a','b','b','c'],
                     ['a','d','e','e'],
                     ['f','d','g','g'],
                     ['f','h','i','i']],
                 [['a', 6,'*'],
                  ['b',3,'-'],
                  ['c',3,'='],
                  ['d',5,'+'],
                  ['e',3,'-'],
                  ['f',3, '-'],
                  ['g',2,'/'],
                  ['h',4,'='],
                  ['i',1,'-']])

puzzle1partial=Puzzle(4, [['a','b','b','c'],
                          ['a',2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

# a partial solution to puzzle1 with a cage partially filled in
puzzle1partial2=Puzzle(4, [[Guess('a',2),'b','b','c'],
                          ['a',2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

# a partial solution to puzzle1 with a cage partially filled in
#   but not yet verified 
puzzle1partial3=Puzzle(4, [[Guess('a',2),'b','b','c'],
                          [Guess('a',3),2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

# The solution to puzzle 1
puzzle1soln=Puzzle(4, [[2,1,4,3],[3,2,1,4],[4,3,2,1],[1,4,3,2]], [])

puzzle2=Puzzle(6,[['a','b','b','c','d','d'],
                  ['a','e','e','c','f','d'],
                  ['h','h','i','i','f','d'],
                  ['h','h','j','k','l','l'],
                  ['m','m','j','k','k','g'],
                  ['o','o','o','p','p','g']],
               [['a',11,'+'],
                ['b',2,'/'],
                ['c',20,'*'],
                ['d',6,'*'],
                ['e',3,'-'],
                ['f',3,'/'],
                ['g',9,'+'],
                ['h',240,'*'],
                ['i',6,'*'],
                ['j',6,'*'],
                ['k',7,'+'],
                ['l',30,'*'],
                ['m',6,'*'],
                ['o',8,'+'],
                ['p',2,'/']])
                
#  The solution to puzzle 2
puzzle2soln=Puzzle(6,[[5,6,3,4,1,2],
                      [6,1,4,5,2,3],
                      [4,5,2,3,6,1],
                      [3,4,1,2,5,6],
                      [2,3,6,1,4,5],
                      [1,2,5,6,3,4]], [])


puzzle3=Puzzle(2,[['a','b'],['c','b']],[['b',3,'+'],
                                       ['c',2,'='],
                                       ['a',1,'=']])

puzzle3partial=Puzzle(2,[['a',Guess('b',1)],['c',Guess('b',2)]],
                      [['b',3,'+'],
                       ['c',2,'='],
                       ['a',1,'=']])
                  
puzzle3soln=Puzzle(2,[[1,2],[2,1]],[])                  
                  
# part a)

def read_puzzle(fname):
    '''
    reads information from fname file and returns the info as Puzzle value.

    read_puzzle: Str -> Puzzle
    '''
def read_puzzle(fname):
    '''
    reads information from fname file and returns the info as Puzzle value.

    read_puzzle: Str -> Puzzle
    '''
    b = []
    c = []
    file = open(fname, "r")
    size = int(file.readline()) 
     
    next_line = file.readline()
    
    Len = len(next_line)
    while (next_line != ""):
        if len(next_line) == Len:
            lst_line = next_line.split()
            b.append(lst_line)
            next_line = file.readline()
        else:
            new_lst = next_line.split()
            p = int(new_lst.pop(1))
            new_lst.insert(1,p)
            c.append(new_lst)
            next_line = file.readline()
    file.close()  
    return Puzzle(size, b, c)    

check.expect("Ta2",read_puzzle("inp2.txt"),puzzle3)
check.expect("Ta1",read_puzzle("inp1.txt"),puzzle1)

#part b)

def print_sol(puz, fname):
    '''
    prints the Puzzle puz in fname file
    
    print_sol: Puzzle Str -> None
    '''
    size = puz.size
    brd = puz.board
    out = open(fname, "w")
    
    for i in range(size):
        board = list(map(lambda num: str(num)+"  ", brd[i]))
        board[-1] = str(int(board[-1]))
        out.writelines(board)
        out.write("\n")
    out.close()    
        
    
    
    
    
    
        
    
    
check.set_file_exact("out1.txt", "result1.txt")
check.expect("Tb1", print_sol(puzzle1soln, "out1.txt"), None)

check.set_file_exact("out2.txt", "result2.txt")
check.expect("Tb2", print_sol(puzzle2soln, "out2.txt"), None)

    
#part c)

def find_blank(puz):
    '''
    returns the position of the first blank space in puz, or False if no cells 
    are blank.  If the first constraint has only guesses on the board, 
    find_blank returns 'guess'.  
    
    find_blank: Puzzle -> (anyof Posn False 'guess')
    
    Examples:
    find_blank(puzzle1) => Posn(0 0)
    find_blank(puzzle3partial) => 'guess'
    find_blank(puzzle2soln) => False
    '''
    if puz.constraints == []:
        return False
    for i in range(puz.size):
        for j in range(puz.size):
            if puz.board[i][j] == puz.constraints[0][0]:
                return Posn(j,i)
    return 'guess'
    


check.expect("Tc", find_blank(Puzzle(3, [["b","c","a"],["a","a","a"],
                                          ["d","a","e"]],
                                          [["a",18,"*"],["b",1,"="],["c",2,"="],
                                           ["d",3,"="],["e",1,"="]])), 
             Posn(2,0))





#part d)

def is_guess(g):
    if isinstance(g, Guess):
        return g.number
    else:
        return g

def used_in_row(puz,pos):
    '''
    returns a list of numbers used in the same row as (x,y) position, pos, 
    in the given puz. 
    
    used_in_row: Puzzle Posn -> (listof Nat)
    '''
    #row = puz.board[pos.y]
    #used_row = sorted(list(filter((lambda x : type(x) == int),row)))
    #return used_row   
    
    res_lst1 = list(filter(lambda g:(isinstance(g, Guess)) or \
                               (isinstance(g, int)),puz.board[pos.y]))    
    
    res_lst2 =sorted(list(map(is_guess, res_lst1)))
    return res_lst2
        
    


check.expect("Td1", used_in_row(puzzle1,Posn(1,1)), [])
check.expect("Td2", used_in_row(Puzzle(4,[[4,'b','b',1],[Guess('a',2),'a',1,4],
                                          ['a','a','a','a'],[1,4,2,3]],
                                       [['a',144,'*'],['b',5,'+']])
                                       ,Posn(1,1)), [1,2,4])




def used_in_col(puz,pos):
    '''
    returns a list of numbers used in the same column as (x,y) position, pos, 
    in the given puz. 
    
    used_in_col: Puzzle Posn -> (listof Nat)
    '''
    col = pos.x
    is_col = []
    for i in range(len(puz.board)):
        yes_col = puz.board[i][col]
        is_col.append(yes_col)
       
    lst = sorted(list(filter((lambda x: type(x) == int), is_col)))
       
    return lst    
    
    

 
check.expect("Td3", used_in_col(puzzle1partial2,Posn(1,0)), [2,3])  
check.expect("Td4", used_in_col(puzzle2soln,Posn(3,5)), [1,2,3,4,5,6])  



#part e)


def available_vals(puz,pos):
    '''
    returns a list of valid entries for the (x,y) position, pos, 
    of the consumed puzzle, puz.
    
    available_vals: Puzzle Posn -> (listof Nat)
    '''
    size = puz.size
    row = used_in_row(puz,pos)
    col = used_in_col(puz,pos)
    
    
    available_lst = list(filter((lambda x: not(x in row) and not(x in col)),\
                                range(1,size+1)))
    return available_lst


check.expect("Te1", available_vals(puzzle1partial, Posn(2,2)), [2,4])
check.expect("Te2", available_vals(Puzzle(4, [['b','b',Guess('a',3),
                                               Guess('a',1)],
                                              ['b',3,'a','a'],
                                              [3,1,'a',2],
                                              [1,4,'a',3]],
                                          [['a',15,'+'],['b',8,'+']]),
                                   Posn(2,1)), [1,2,4])



# part f)  

def place_guess(brd,pos,val):
    '''
    fills in the (x,y) position, pos, of the board, brd, with the a guess with 
    value, val
    
    place_guess: (listof (listof (anyof Str Nat Guess))) Posn Nat 
                       -> (listof (listof (anyof Str Nat Guess)))
    '''
    
    res=copy.deepcopy(brd) # a copy of brd is assigned to res without any 
                           # aliasing to avoid mutation of brd. 
                           #  You should update res and return it
    temp = res[pos.y][pos.x]
    res[pos.y][pos.x] = Guess(temp,val)
    
    return res

check.expect("Tf1", place_guess(puzzle3.board, Posn(1,1),2), 
             [['a','b'],['c',Guess('b',2)]])
check.expect("Tf2", place_guess(puzzle1partial2.board, Posn(0,1),3), 
             puzzle1partial3.board)


#  **********  DO NOT CHANGE THIS FUNCTION ******************


def fill_in_guess(puz, pos, val):
    '''
    fills in the pos Position of puz's board with a guess with value val
    
    fill_in_guess: Puzzle Posn Nat -> Puzzle
    '''
    
    res=Puzzle(puz.size, copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    tmp=copy.deepcopy(res.board)
    res.board=place_guess(tmp, pos, val)
    return res
''' 
check.expect("Tf3", fill_in_guess(puzzle1, Posn(3,2),5), 
             Puzzle(4,[['a','b','b','c'],
                      ['a','d','e','e'],
                      ['f','d','g',Guess('g',5)],
                      ['f','h','i','i']], puzzle1.constraints))
             
'''

# part g)


def guess_valid(puz):
    '''
    determines if the guesses in puz satisfy their constraint
    
    guess_valid: Puzzle -> Bool

    '''
    board = puz.board
    prev_guess = list(map(lambda lst: list(filter\
                                           (lambda n: type(n) == Guess,lst))
                          ,board))
    
    guesses = []
    valid = puz.constraints[0][1]
    
    for lst in prev_guess:
        for elem in lst:
            guesses = guesses + [elem]
    
    guess_n = list(map(lambda n : n.number, guesses))
    
    if puz.constraints[0][2] == "/" :
        a = guess_n[1]/guess_n[0]
        b = guess_n[0]/guess_n[1]
        return (a == valid or b == valid)
    
    if puz.constraints[0][2] == "-" :
        return abs(guess_n[0] - guess_n[1]) == valid
    
    if puz.constraints[0][2] == "+":
        return sum(guess_n) == valid
    
    if puz.constraints[0][2] == "*":
        c = 1
        for n in guess_n:
            c = c*n
        return c == valid
    if puz.constraints[0][2] == "=":
        return guess_n[0] == valid

check.expect("Tg1", guess_valid(puzzle3partial), True)
check.expect("Tg2", guess_valid(Puzzle(2,[[Guess('a',2),Guess('a',1)],
                                          [Guess('a',1),Guess('a',2)]],
                                       [['a',4,'+']])), False)
check.expect("Tg3", guess_valid(Puzzle(2,[[Guess('a',2),Guess('a',1)],
                                          [Guess('a',1),Guess('a',2)]],
                                       [['a',4,'*']])), True)


                 
# part h) 

def apply_guess(puz):
    '''
    converts all guesses in puz into their corresponding numbers and removes 
    the first contraint from puz's list of contraints
    
    apply_guess:  Puzzle -> Puzzle
    '''
    
    res=Puzzle(puz.size, copy.deepcopy(puz.board), 
                             copy.deepcopy(puz.constraints))
                   # a copy of puz is assigned to res without any 
                   # aliasing to avoid mutation of puz. 
                   #  You should update res and return it
    cons = res.constraints
    brd = res.board
    size = res.size
    
    
    for x in range(size):
        for y in range(size):
            if type(brd[x][y]) == Guess:
                    if brd[x][y].symbol == cons[0][0]:
                        brd[x][y] =  brd[x][y].number
    
    cons.pop(0)
    return res
            
            
    

check.expect("Th1", apply_guess(Puzzle(6,[[5,6,3,4,1,2],[6,1,4,5,2,3],
                                          [4,5,2,3,6,1],[3,4,1,2,5,6],
                                          [2,3,6,1,4,5],
                                          [1,2,5,Guess('p',6),Guess('p',3),4]],
                                       [['p',2,'/']])), puzzle2soln)
              


# part i)


def neighbours(puz):
    '''
    returns a list of next puzzles after puz in the implicit graph
    
    neighbours: Puzzle -> (listof Puzzle)
    '''
    
    tmp=Puzzle(puz.size, copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    # a copy of puz is assigned to tmp without any 
    # aliasing to avoid mutation of puz.
    
   
        
    pos  = find_blank(tmp)
    
    if pos=='guess':
        if guess_valid(tmp):
            return [apply_guess(tmp)]    
    if pos=='guess':
        return []               
    if pos  == False:
        return [] 
    
    neighbours = list(map(lambda x: fill_in_guess(tmp,pos,x),available_vals\
                          (tmp,pos)))
    return neighbours
    
     
    
    
    
    
    
check.expect("Ti1", neighbours(puzzle2soln), [])
check.expect("Ti2", neighbours(puzzle3), [Puzzle(2,[['a',Guess('b',1)],
                                                    ['c','b']],
                                                 [['b',3,'+'], ['c',2,'='],
                                                  ['a',1,'=']]),
                                          Puzzle(2,[['a',Guess('b',2)],
                                                    ['c','b']],[['b',3,'+'],
                                                                ['c',2,'='],
                                                                ['a',1,'=']])])
puz1=Puzzle(4,[[4,2,'a','a'],['b', Guess('c',3),'a',4],
               ['b', Guess('c',1),Guess('c',4),2],
               [1,Guess('c',4),Guess('c',2),3]],
            [['c',96,'*'],['b',5,'+'],['a',3,'*']])
puz2=Puzzle(4,[[4,2,'a','a'],['b',3,'a',4],['b',1,4,2],
               [1,4,2,3]],[['b',5,'+'],['a',3,'*']])
check.expect("Ti3",neighbours(puz1),[puz2])



# ******** DO NOT CHANGE THIS PART ***************


def solve_kenken(orig):
    '''
    finds the solution to a KenKen puzzle, orig, or returns False 
    if there is no solution.  
    
    solve-kenken: Puzzle -> (anyof Puzzle False)
    '''
    
    to_visit=[]
    visited=[]
    to_visit.append(orig)
    while to_visit!=[] :
        if find_blank(to_visit[0])==False:
            return to_visit[0]
        elif to_visit[0] in visited:
            to_visit.pop(0)
        else:
            nbrs = neighbours(to_visit[0])
            new = list(filter(lambda x: x not in visited, nbrs))
            new_to_visit=new + to_visit[1:] 
            new_visited= [to_visit[0]] + visited
            to_visit=new_to_visit
            visited=new_visited
            
    return False

'''
check.expect("game1",solve_kenken(puzzle3partial),False)
check.expect("game2",solve_kenken(puzzle1), puzzle1soln)
check.expect("game3",solve_kenken(puzzle2), puzzle2soln)
check.expect("game4",solve_kenken(puzzle3), puzzle3soln)
check.expect("game5",solve_kenken(puzzle3soln), puzzle3soln)
'''
