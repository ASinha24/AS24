even_numbers=[x for x in range(1,101) if x%2==0]
print(even_numbers)
odd_numbers=[y for y in range(1,101,2)]
print(odd_numbers)

words=["the","quick","brown","fox","jumps","over","the","lazy","dog"]
answer=[[w.lower(),w.upper(),len(w)] for w in words]
print(answer)
