if __name__ == '__main__':
    def output():
        new = []
        for i in range(int(input())):
            name = input()
            score = float(input())
            new.append([name,score])
        for j in new:
            print(max(j, key=lambda j : j[1]))
            
                        
output()

