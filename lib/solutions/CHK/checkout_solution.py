

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    prices = {'A': 50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20,'H':10,'I':35,'J':60,'K':70,'L':90,'M':15,'N':40,'O':10,'P':50,'Q':30,'R':50,'S':20,'T':20,'U':40,'V':50,'W':20,'X':17,'Y':20,'Z':21}


    special_offers = {'A': [(5,200),(3,130)], 'B':[(2,45)], 'E':[(2,80)], 'F':[(3,20)], 'H':[(10,80),(5,45)],'K':[(2,120)],'N':[(3,120)],'P':[(5,200)],'Q':[(3,80)],'R':[(3,150)],'U':[(4,120)],'V':[(3,130),(2,90)], 'group_discount':(['S','T','X','Y','Z'],3,45) }

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
    

    group_size = special_offers['group_discount'][1]
    group_items = special_offers['group_discount'][0]
    group_price = special_offers['group_discount'][2]
    group_count = sum(item_counts.get(item,0) for item in group_items)
    group_offer_count = group_count//group_size
    total_cost += group_offer_count*group_price

    if group_offer_count>0:
        sorted_group_items = sorted(group_items, key=lambda item:prices[item], reverse=True)
        items_to_deduct = group_offer_count * group_size
        for item in sorted_group_items:
            while items_to_deduct>0 and item_counts.get(item,0) > 0:
                item_counts[item] -=1
                items_to_deduct -=1
                if items_to_deduct ==0:
                    break

    for item, count in item_counts.items():
        if item in special_offers and item not in ['F','U','N','R']:
            for offer in sorted(special_offers[item], key=lambda x: x[0], reverse=True):
                offer_count, offer_price = offer
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
    assert checkout("**") == -1

    assert checkout("F") == 10
    assert checkout("FFFF") == 30
    assert checkout("FFFFF") == 40
    assert checkout("BBBEEEFFFF") == 195

    assert checkout("VVV") == 130
    assert checkout("UUUU") == 120
    assert checkout("VVVV") == 180
    assert checkout("VVUUUUQQQ") == 290

    assert checkout("K") == 70
    #assert checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965

    assert checkout("STX") == 45
    assert checkout("STXYZ") == 82

test_checkout()

