# exam: 04. Generating 0/1 Vectors
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#3

def gen_vector(vector, idx):
    # BASE CASE: Stop when fill the last index of array and print the result vector
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        # Recursive call
        gen_vector(vector, idx + 1)


vector_size = int(input())
vector = [None] * vector_size

gen_vector(vector, 0)
