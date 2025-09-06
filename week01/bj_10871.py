n, x = map(int, input().split())
elements = list(map(int, input().split()))
selected_elements = [str(element) for element in elements if element < x]
print(" ".join(selected_elements))