if __name__ == "__main__":
    cents = [50, 25, 10, 5, 1]
    ways = [0]*8192
    ways[0] = 1

    for i in range(5):
        for j in range(cents[i],8192):
            ways[j] = ways[j] + ways[j - cents[i]]
    
    amout = input("Enter amout:")
    print(ways[int(amout)])
    
