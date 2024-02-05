import math

class P:
    def __init__(self, num):
        self.num = num
        self.solution = None
        
    def solve(self):
        return self.solution
    
    def is_prime(self, num):
        
        rt = int(math.sqrt(num))
        i = 2
        while i <= rt:
            if num%i==0:
                return False
            i+=1
        return True
        

class P852(P):
    def __init__(self, N=50, p1=0.5, p2=0.75):
        
        super().__init__(852)
        
        self.N = N
        self.p1 = p1
        self.p2 = p2
        self.awarded = 20
        self.penalized = -50
        self.guesspen = -1
        
    def solve(self):
        # code here
        return self.solution
    
class P1(P):
    def __init__(self, limit = 1000, nums = [3,5]):
        super().__init__(1)
        self.limit = limit
        self.num1 = nums[0]
        self.num2 = nums[1]

    def solve(self):
        # code here
        i = 1
        suma = 0
        while i < self.limit:
            if not i % self.num1 or not i % self.num2:
                suma += i
            i+=1
        self.solution = suma
        
        return self.solution
    
class P2(P):
    def __init__(self, limit = 4000000):
        super().__init__(2)
        self.limit = limit
        
    def solve(self):
        # code here
        prev = 1
        tek = 1
        suma = 0
        while tek < self.limit:
            nxt = prev + tek
            if not nxt % 2:
                suma += nxt
            prev = tek
            tek = nxt
            
        self.solution = suma
        return self.solution
        
    
class P3(P):
    def __init__(self, num = 600851475143):
        super().__init__(3)
        self.num = num
        
    def solve(self):
        # code here
        lpf = 1
        rt = int(math.sqrt(self.num)+1)
        lower = 0
        i = 2
        while i <= rt:
            if self.num % i == 0:
                k = 2
                krt = int(math.sqrt(i)+1)
                b = True
                while k <= krt:
                    if i % k == 0:
                        b = False
                        break
                    k+=1
                if b:
                    lpf = i
            i+=1
        
        self.solution = lpf
        return self.solution
    
    
class P4(P):
    def __init__(self, limit = 999):
        super().__init__(4)
        self.limit = limit

    def solve(self):
        # code here

        rez = ""
        result = 0
        for i in reversed(range(100,self.limit)):
            for j in reversed(range(100,self.limit)):
                rez = str(i*j)
                b = True
                for k in range(len(rez)//2):
                    if rez[k] != rez[-k-1]:
                        b = False
                        break
                if b:
                    if result < int(rez): 
                        result = int(rez)
        self.solution = result
        return self.solution
    
    
class P5(P):
    def __init__(self, limit = 20):
        super().__init__(5)
        self.limit = limit

    def solve(self):
        # code here

        result = 2*3*5*7*11*13*17*19*2*2*3*2
        
        self.solution = result
        return self.solution
    

    
class P6(P):
    def __init__(self, n = 100):
        super().__init__(6)
        self.n = n

    def solve(self):
        # code here

        result = ((self.n+1)*(self.n)/2)**2 - self.n*(self.n+1)*(2*self.n+1)/6
        
        self.solution = result
        return self.solution
    
    
class P7(P):
    def __init__(self, no = 10001):
        super().__init__(7)
        self.no = no

    def solve(self):
        # code here

        result = 0
        k = 0
        i = 2
        while True:
            if self.is_prime(i):
                k+=1
                if k == self.no:
                    result = i
                    break
            i+=1
        
        
            
        
        self.solution = result
        return self.solution


class P8(P):
    def __init__(self, lista = [
                                "73167176531330624919225119674426574742355349194934",
                                "96983520312774506326239578318016984801869478851843",
                                "85861560789112949495459501737958331952853208805511",
                                "12540698747158523863050715693290963295227443043557",
                                "66896648950445244523161731856403098711121722383113",
                                "62229893423380308135336276614282806444486645238749",
                                "30358907296290491560440772390713810515859307960866",
                                "70172427121883998797908792274921901699720888093776",
                                "65727333001053367881220235421809751254540594752243",
                                "52584907711670556013604839586446706324415722155397",
                                "53697817977846174064955149290862569321978468622482",
                                "83972241375657056057490261407972968652414535100474",
                                "82166370484403199890008895243450658541227588666881",
                                "16427171479924442928230863465674813919123162824586",
                                "17866458359124566529476545682848912883142607690042",
                                "24219022671055626321111109370544217506941658960408",
                                "07198403850962455444362981230987879927244284909188",
                                "84580156166097919133875499200524063689912560717606",
                                "05886116467109405077541002256983155200055935729725",
                                "71636269561882670428252483600823257530420752963450"
                                ], k = 13):
        super().__init__(8)
        self.lista = lista
        self.k = k

    def solve(self):
        # code here

        conc = ""
        for x in self.lista:
            conc += x

        maxprod = 1
        lastnum = 1
        curprod = 1
       
        for i in range(self.k):
            curprod *= int(conc[i])
            if maxprod < curprod:
                maxprod = curprod
    
        i = self.k
        while i < len(conc):
            n = int(conc[i])
            if n:
                curprod *= n
                curprod /= 1


        for i in range(self.k,len(conc)):
            if lastnum == 0:
                curprod = int(conc[i-3])*int(conc[i-2])*int(conc[i-1])
            else:
                curprod //= lastnum
            lastnum = int(conc[i])
            curprod *= lastnum
            if curprod > maxprod:
                maxprod = curprod
        
        self.solution = maxprod
        return self.solution
