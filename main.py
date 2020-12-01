import matplotlib.pyplot as plt
import classDef

def play(player1, player2):
    str1 = player1.determineStrategy(player2)
    str2 = player2.determineStrategy(player1)
    if str1 == str2 == 0:
        payoff = 0
        player1.addPayoff(player2, payoff)
        player2.addPayoff(player1, payoff)

    elif str1 == str2 == 1:
        payoff = 2
        player1.addPayoff(player2, payoff)
        player2.addPayoff(player1, payoff)
    elif str1 > str2:
        payoff1 = 3
        payoff2 = -1
        player1.addPayoff(player2, payoff2)
        player2.addPayoff(player1, payoff1)
    else:
        payoff1 = 3
        payoff2 = -1
        player1.addPayoff(player2, payoff1)
        player2.addPayoff(player1, payoff2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p1 = classDef.Player1()
    p2 = classDef.Player2()
    p3 = classDef.Player3()
    p4 = classDef.Player4()
    p5 = classDef.Player5()

    playerlst = [p1, p2, p3, p4,p5]
    turns = 60
    x = list(range(1,turns+1))
    #print(x)
    for i in playerlst:
        for j in playerlst:
            if i != j:
                for k in range(turns):
                    play(i,j)
                    
#print(p3.strategies["player4"])
#print(len(p3.payoffrec["player4"]))

x2 = list(range(1,turns*2 + 1))
#plotting data
'''
fig, (ax1,ax2) = plt.subplots(2)
ax1.plot(x2,p3.payoffrec["player2"][:turns*2],'k',label = '3vs2')
ax1.plot(x2,p1.payoffrec["player2"][:turns*2],'b',label = "1vs2")
ax1.plot(x2,p4.payoffrec["player2"][:turns*2],'r',label = '4vs2')
#print(p5.strategies["player2"][0:turns])
#print(p2.strategies["player5"][0:turns])
#legend = ax1.legend(loc = "upper left", shadow=True)
ax1.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
'''
'''
ax2.plot(x2,p5.payoffrec["player1"][0:turns*2],'b',label = '5vs1')
ax2.plot(x2,p5.payoffrec["player2"][0:turns*2],'r',label = '5vs2')
ax2.plot(x2,p5.payoffrec["player3"][0:turns*2],'k',label = '5vs3')
ax2.plot(x2,p5.payoffrec["player4"][0:turns*2],'purple',label = '5vs4')
#legend = ax2.legend(loc = "upper left", shadow=True)
ax2.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
print(p1.payoff,p2.payoff,p3.payoff,p4.payoff,p5.payoff)
#print(p1.strategies["player5"])
#print(p5.strategies["player1"])
'''

plt.plot(x2,p3.payoffrec["player4"][:turns*2],'r',label = '3vs2')
plt.plot(x2,p1.payoffrec["player4"][:turns*2],'k',label = '1vs2')
plt.plot(x2,p2.payoffrec["player4"][:turns*2],'b',label = '4vs2')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.title("Payoff Curves")
print(p1.payoff,p2.payoff,p3.payoff,p4.payoff,p5.payoff)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
