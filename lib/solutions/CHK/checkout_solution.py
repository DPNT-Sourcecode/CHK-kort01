

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    prices = {'A': 50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10}
    special_offers = {'A': [(3,130),(5,200)], 'B':[(2,45)], 'E':[(2,80)], 'F':[(3,20)]}

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

    for item, count in item_counts.items():
        if item in special_offers and item != 'F':
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

    assert checkout("BBBEEEFFFF") == 195

test_checkout()



