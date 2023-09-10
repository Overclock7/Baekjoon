# https://www.acmicpc.net/problem/4673

def self_number():
    num_set = set(range(1, 10001))
    not_self_num = set()
    
    for num in range(1, 10001):
        for each_num in str(num): #str(num)은 리스트이다.
            num += int(each_num)
            
        not_self_num.add(num)  #set은 중복을 허용하지 않음
        
    return sorted(num_set - not_self_num)

if __name__ == "__main__":
    self_numbers = self_number()
    
    for self_num in self_numbers:
        print(self_num)
