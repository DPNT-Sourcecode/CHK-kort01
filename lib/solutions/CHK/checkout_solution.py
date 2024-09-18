

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    prices = {'A': 50, 'B':30, 'C':20, 'D':15, 'E':40}
    special_offers = {'A': [(3,130),(5,200)], 'B':[(2,45)], 'E':[(2,80)]}

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

    for item, count in item_counts.items():
        if item in special_offers:
            for offer_count, offer_price in sorted(special_offers[item], reverse=True):
                total_cost += (count // offer_count)*offer_price
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
    assert checkout("BBBEEE") == 160

test_checkout()


