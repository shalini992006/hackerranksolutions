def can_stack(blocks):
    top = float('inf')
    i, j = 0, len(blocks) - 1
    while i <= j:
        if blocks[i] >= blocks[j]:
            pick = blocks[i]
            i += 1
        else:
            pick = blocks[j]
…    print(can_stack(blocks))
   
