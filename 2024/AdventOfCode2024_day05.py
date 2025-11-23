
# READ DATA
with open('./2024/05.txt', 'r', encoding='utf-8') as f:
    INPUT = f.read()

INPUT_RULES = INPUT.split('\n\n')[0].split('\n')
INPUT_UPDATES = INPUT.split('\n\n')[1].split('\n')

# Filter out empty strings
INPUT_RULES = [el for el in INPUT_RULES if el.strip()]
INPUT_UPDATES = [el for el in INPUT_UPDATES if el.strip()]

INPUT_RULES = [el.split("|") for el in INPUT_RULES]
INPUT_UPDATES = [el.split(",") for el in INPUT_UPDATES]

for rule in INPUT_RULES:
    for i in range(len(rule)):
        rule[i] = int(rule[i])

for update in INPUT_UPDATES:
    for i in range(len(update)):
        update[i] = int(update[i])

# DAY 5 PUZZLE 1
res1 = 0

for update in INPUT_UPDATES:
    rules_accomplished = True
    for rule in INPUT_RULES:
        if (rule[0] in update) and (rule[1] in update):
            index_of_rule_0 = update.index(rule[0])
            index_of_rule_1 = update.index(rule[1])
            if index_of_rule_0 > index_of_rule_1:
                rules_accomplished = False
    if rules_accomplished:
        middle_value = update[len(update) // 2]
        res1 += middle_value

print('DAY 5 PUZZLE 1: %d' % (res1))

# DAY 5 PUZZLE 2
res2 = 0

for update in INPUT_UPDATES:
    # Check if this update violates any rules
    violates_rules = False
    for rule in INPUT_RULES:
        if (rule[0] in update) and (rule[1] in update):
            index_of_rule_0 = update.index(rule[0])
            index_of_rule_1 = update.index(rule[1])
            if index_of_rule_0 > index_of_rule_1:
                violates_rules = True
                break
    
    # Only process updates that violate rules
    if violates_rules:
        # Create a copy to reorder
        reordered_update = update.copy()
        
        # Keep reordering until all rules are satisfied
        changed = True
        while changed:
            changed = False
            for rule in INPUT_RULES:
                if (rule[0] in reordered_update) and (rule[1] in reordered_update):
                    index_of_rule_0 = reordered_update.index(rule[0])
                    index_of_rule_1 = reordered_update.index(rule[1])
                    # If rule[0] is after rule[1], swap them
                    if index_of_rule_0 > index_of_rule_1:
                        # Swap the elements
                        reordered_update[index_of_rule_0], reordered_update[index_of_rule_1] = reordered_update[index_of_rule_1], reordered_update[index_of_rule_0]
                        changed = True
        
        # Add the middle value of the reordered update
        middle_value = reordered_update[len(reordered_update) // 2]
        res2 += middle_value

print('DAY 5 PUZZLE 2: %d' % (res2))