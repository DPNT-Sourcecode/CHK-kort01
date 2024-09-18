

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    prices = {'A': 50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20,'H':10,'I':35,'J':60,'K':70,'L':90,'M':15,'N':40,'O':10,'P':50,'Q':30,'R':50,'S':30,'T':20,'U':40,'V':50,'W':20,'X':90,'Y':10,'Z':50}
    special_offers = {'A': [(5,200),(3,130)], 'B':[(2,45)], 'E':[(2,80)], 'F':[(3,20)], 'H':[(10,80),(5,45)],'K':[(2,150),'N':[(3,120),'P':[(5,200),'Q':[(3,80),'R':[(3,150),'U':[(4,120),'V':[(3,130),(2,90)] }

    total_cost, item_counts = 0, {}

    if not skus:
        return 0
    
    for item in skus:
        if item not in prices:
            return -1
        item_counts[item] = item_counts.get(item, 0) +1
    
    
    if 'E' in item_counts and item_counts['E'] >=2:
        free_b_count = item_counts['E'] // 2
        if 'B' in item_counts:
            item_counts['B'] = max(0, item_counts['B'] -free_b_count)
        
    if 'F' in item_counts:
        f_count = item_counts['F']
        free_f_count = f_count//3
        paid_f_count = f_count - free_f_count
        item_counts['F'] = paid_f_count
    
    if 'N' in item_counts and item_counts['N'] >=3:
        free_m_count = item_counts['N'] // 3
        if 'M' in item_counts:
            item_counts['M'] = max(0, item_counts['M'] -free_m_count)
    
    if 'R' in item_counts and item_counts['R'] >=3:
        free_q_count = item_counts['R'] // 3
        if 'Q' in item_counts:
            item_counts['Q'] = max(0, item_counts['Q'] -free_q_count)
    
    if 'U' in item_counts:
        u_count = item_counts['U']
        free_u_count = u_count//4
        paid_u_count = u_count - free_u_count
        item_counts['U'] = paid_u_count

    for item, count in item_counts.items():
        if item in special_offers and item not in ['F','U','N','R']:
            for offer_count, offer_price in sorted(special_offers[item], reverse=True):
                applicable_offers = count // offer_count
                total_cost += applicable_offers*offer_price
                count %= offer_count
            
            total_cost += count*prices[item]
        else:
            total_cost += count*prices[item]
    
    
    return total_cost

def test_checkout():
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("ABCD") == 115
    assert checkout("ABCDE") == 155
    assert checkout("AAA") == 130
    assert checkout("AAAAA") == 200
    assert checkout("BB") == 45
    assert checkout("BBBEEE") == 165
    assert checkout("X") == -1

    assert checkout("F") == 10
    assert checkout("FFFF") == 30
    assert checkout("FFFFF") == 40
    assert checkout("BBBEEEFFFF") == 195

test_checkout()

