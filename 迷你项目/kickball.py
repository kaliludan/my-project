#coding=utf-8

print "罚点球！"

gameover=False
over=0
score=0

while gameover==False:

    print '\n选择一个方向射门\n1向左；2中间；3向右.'
    player=input()
    l=['左边','中间','右边']
    x=l[player-1]
    print '你踢向了 ' + x

    from random import choice
    direction=['左边','中间','右边']
    com=choice(direction)
    print '守门员扑向了 '+com
    
    if com==x:
        print '你的射门被扑出去了！'
        over=over-1
    else:
        print '进门了!'
        score=score+1
            
    if over==-3:
        print 'Game Over'
        print '你的分数是 %d'%(score)
        gameover=True