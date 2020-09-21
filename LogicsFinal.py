import random
def gameStart():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_random2(mat):
    x=random.randint(0,3)
    y=random.randint(0,3)
    while (mat[x][y]!=0):
        x=random.randint(0,3)
        y=random.randint(0,3)
    mat[x][y]=2

def get_current_state(mat):
    for r in range(4):
        for c in range(4):
            if mat[r][c]==2048:
                return "WON"

    for r in range(4):
        for c in range(4):
            if mat[r][c]==0:
                return "GAME NOT OVER"

    for r in range(3):
        for c in range(3):
            if mat[r][c]==mat[r][c+1] or mat[r][c]==mat[r+1][c]:
                return "GAME NOT OVER"
    for c in range(3):
        if mat[3][c]==mat[3][c+1]:
            return "GAME NOT OVER"
    for r in range(3):
        if mat[r][3]==mat[r+1][3]:
            return "GAME NOT OVER"

    return "LOST"

def compress(mat):
    new_mat=[]
    change=False
    for i in range(4):
        new_mat.append([0]*4)

    for r in range(4):
        pos=0
        for c in range(4):
            if mat[r][c]!=0:
                new_mat[r][pos]=mat[r][c]
                if c!=pos:
                    change=True
                pos=pos+1
    return new_mat,change

def merge(mat):
    change=False
    for r in range(4):
        for c in range(3):
            if mat[r][c]==mat[r][c+1] and mat[r][c]!=0:
                mat[r][c]=mat[r][c]*2
                mat[r][c+1]=0
                change=True
    return mat,change


def reverse(mat):
    new_mat=[]

    for r in range(4):
        new_mat.append([])
        for c in range(4):
            new_mat[r].append(mat[r][4-c-1])
    return new_mat

def transpose(mat):
    new_mat=[]
    for r in range(4):
        new_mat.append([])
        for c in range(4):
            new_mat[r].append(mat[c][r])
    return new_mat


def moveleft(grid):
    newgrid,change1=compress(grid)
    newgrid,change2=merge(newgrid)
    changed=change1 or change2
    newgrid,tenp=compress(newgrid)
    return newgrid,changed

def moveright(grid):
    reverse_grid=reverse(grid)
    newgrid,change1=compress(reverse_grid)
    newgrid,change2=merge(newgrid)
    changed=change1 or change2
    newgrid,temp=compress(newgrid)
    finalgrid=reverse(newgrid)
    return finalgrid,changed

def moveup(grid):
    transposegrid=transpose(grid)
    newgrid,change1=compress(transposegrid)
    newgrid,change2=merge(newgrid)
    changed=change1 or change2
    newgrid,temp=compress(newgrid)
    finalgrid=transpose(newgrid)
    return finalgrid,changed

def movedown(grid):
    transposegrid=transpose(grid)
    reversegrid=reverse(transposegrid)
    newgrid,change1=compress(reversegrid)
    newgrid,change2=merge(newgrid)
    changed=change1 or change2
    newgrid,temp=compress(newgrid)
    finalreversegrid=reverse(newgrid)
    finalgrid=transpose(finalreversegrid)
    return finalgrid,changed






















