import random


class Player1():  # cheater
    def __init__(self):
        self.name = 'player1'
        self.strategies = {}  # previous strategies
        self.payoff = 0
        self.payoffrec = {}

    def determineStrategy(self, other):
        try:
            self.strategies[other.name].append(0)
        except:
            self.strategies[other.name] = [0]
        return 0

    def addPayoff(self, other, payoff):
        self.payoff += payoff
        try:
            self.payoffrec[other.name].append(self.payoffrec[other.name][-1] + payoff)
        except:
            self.payoffrec[other.name] = [payoff]
        


class Player2():
    def __init__(self):
        self.name = 'player2'
        self.strategies = {}  # previous strategies
        self.payoff = 0
        self.payoffrec = {}
        self.tolerance = 2

    def determineStrategy(self, other):
        count = 0
        try:
            for i in other.strategies[self.name]:
                if i == 0:
                    count += 1
            if count <= self.tolerance:
                try:
                    self.strategies[other.name].append(1)
                except:
                    self.strategies[other.name] = [1]
                return 1
            self.strategies[other.name].append(other.strategies[self.name][-1])
            return other.strategies[self.name][-1]
        except:
            self.strategies[other.name] = [1]
            return 1

    def addPayoff(self, other, payoff):
        self.payoff += payoff
        try:
            self.payoffrec[other.name].append(self.payoffrec[other.name][-1] + payoff)
        except:
            self.payoffrec[other.name] = [payoff]
        


class Player3():  # once cheated, always cheat
    def __init__(self):
        self.name = 'player3'
        self.strategies = {}  # previous strategies
        self.payoff = 0
        self.payoffrec = {}

    def determineStrategy(self, other):
        if other.name in self.strategies.keys():
            if 0 in other.strategies[self.name]:
                try:
                    self.strategies[other.name].append(0)
                except:
                    self.strategies[other.name] = [0]
                return 0
            else:
                try:
                    self.strategies[other.name].append(1)
                except:
                    self.strategies[other.name] = [1]
                return 1
        else:
            self.strategies[other.name] = [1]
            #print("first time 1")
            return 1

    def addPayoff(self, other, payoff):
        self.payoff += payoff
        try:
            self.payoffrec[other.name].append(self.payoffrec[other.name][-1] + payoff)
        except:
            self.payoffrec[other.name] = [payoff]

class Player4():  # random probability player
    def __init__(self):
        self.name = 'player4'
        self.strategies = {}  # previous strategies
        self.payoff = 0
        self.payoffrec = {}

    def determineStrategy(self, other):
        prob = random.random()

        if prob >= 0.5:
            strategy = 1
        else:
            strategy = 0
        if other.name not in self.strategies:
            self.strategies[other.name] = [strategy]
        else:
            self.strategies[other.name].append(strategy)
        
        return strategy

    def addPayoff(self, other, payoff):
        self.payoff += payoff
        try:
            self.payoffrec[other.name].append(self.payoffrec[other.name][-1] + payoff)
        except:
            self.payoffrec[other.name] = [payoff]
        
class Player5():
    def __init__(self):
        self.name = 'player5'
        self.strategies = {}  # previous strategies
        self.payoff = 0
        self.payoffrec = {}
        self.oldstr = 1
        self.turns = 0
        self.tolerance = 2
        self.tenspayoff = 0
        self.best = {"player1":3,"player2":3,"player3":2,"player4":1}

    def determineStrategy(self,other):

        #print(other.name)
        if self.turns < 10:
            #print("turns",self.turns)
            if other.name in self.strategies.keys():
                #print("turnssss", self.turns)
                #print("sit1， other last move",other.strategies[self.name][self.turns-1] )
                if other.strategies[self.name][self.turns - 1] == 0:
                    #print("sit3")
                    try:
                        self.strategies[other.name].append(1-self.oldstr)
                    except:
                        self.strategies[other.name] = 1-self.oldstr
                    self.oldstr = 1-self.oldstr
                    self.turns += 1
                    #print("returns", self.oldstr)
                    return self.oldstr
                else:
                    #print("sit4")
                    try:
                        self.strategies[other.name].append(self.oldstr)
                    except:
                        self.strategies[other.name] = self.oldstr
                    self.turns += 1
                    #print("returns", self.oldstr)
                    return self.oldstr
            else:
                #print("sit2")
                self.strategies[other.name] = [1]
            self.turns += 1
            #print("returns", self.oldstr)
            return self.oldstr
        else:
            if self.tenspayoff > 7.44:
                #if self.turns % 59 == 0:
                #    self.turns = 0      

                #print(other.name,"do not change",self.turns)
                if other.name in self.strategies.keys():
                    #print("turns",self.turns)
                    #print("sit1， other last move",other.strategies[self.name][self.turns-1] )
                    if other.strategies[self.name][self.turns%59 - 1] == 0:
                        #print("sit3")
                        try:
                            self.strategies[other.name].append(1-self.oldstr)
                        except:
                            self.strategies[other.name] = 1-self.oldstr
                        self.oldstr = 1-self.oldstr
                        self.turns += 1
                        #print("returns", self.oldstr)
                        return self.oldstr
                    else:
                        #print("sit4")
                        try:
                            self.strategies[other.name].append(self.oldstr)
                        except:
                            self.strategies[other.name] = self.oldstr
                        self.turns += 1
                        #print("returns", self.oldstr)
                        return self.oldstr
                else:
                    #print("sit2")
                    self.strategies[other.name] = [1]
                self.turns += 1
                #print("returns", self.oldstr)
                return self.oldstr               
            else:
                #print(other.name,"change",self.turns)
                #if self.turns % 59 == 0:
                #    self.turns = 0
                if other.name == "player1" or other.name == "player2":
                    #print("change to 3")
                    if other.name in self.strategies.keys():
                        if 0 in other.strategies[self.name]:
                            try:
                                self.strategies[other.name].append(0)
                            except:
                                self.strategies[other.name] = [0]
                            self.turns += 1
                            #print("5 plays 0")
                            return 0
                        else:
                            try:
                                self.strategies[other.name].append(1)
                            except:
                                self.strategies[other.name] = [1]
                            self.turns += 1
                            return 1
                    else:
                        self.strategies[other.name] = [1]
                        self.turns += 1
                        return 1
                elif other.name == "player3":
                    #print("change to 2")
                    count = 0
                    try:
                        for i in other.strategies[self.name]:
                            if i == 0:
                                count += 1
                        if count <= self.tolerance:
                            try:
                                self.strategies[other.name].append(1)
                            except:
                                self.strategies[other.name] = [1]
                            self.turns += 1
                            return 1
                        self.strategies[other.name].append(other.strategies[self.name][-1])
                        self.turns += 1
                        return other.strategies[self.name][-1]
                    except:
                        self.strategies[other.name] = [1]
                        self.turns += 1
                        return 1           
                else:
                    try:
                        self.strategies[other.name].append(0)
                    except:
                        self.strategies[other.name] = [0]
                    self.turns += 1
                    #print("5 plays 1 here")
                    return 0

    def addPayoff(self, other, payoff):
        if self.turns <= 9:
            #print("add", payoff)
            self.tenspayoff += payoff
            #print("now tens is ",self.tenspayoff)
        if self.turns % 60 == 0:
            #print(self.turns, "now")
            #print(self.tenspayoff)
            #print("reset")
            self.tenspayoff = 0
            self.turns = 0
            #print(self.tenspayoff)
        self.payoff += payoff
        try:
            self.payoffrec[other.name].append(self.payoffrec[other.name][-1] + payoff)
        except:
            self.payoffrec[other.name] = [payoff]
'''
a = Player3()
b = Player5()
for i in range(10):
    d = a.determineStrategy((b))
for i in range(10):
    print("round",b.turns)
    c = b.derermineStrategy(a)
print(b.strategies)
print(a.strategies)
'''
