# Example Input


"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def parse_input(input_text):
    # Split the input into rules and updates
    rules_section, updates_section = input_text.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    return rules, updates

def is_update_valid(update, rules):
    # Create a dictionary to map each page to its position
    page_positions = {page: idx for idx, page in enumerate(update)}
    
    # Check each rule
    for X, Y in rules:
        if X in page_positions and Y in page_positions:  # Both pages must be in the update
            if page_positions[X] > page_positions[Y]:  # X must appear before Y
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def process_updates(input_text):
    # Parse input
    rules, updates = parse_input(input_text)
    
    # Process each update and calculate the sum of middle pages
    total_middle_pages = 0
    for update in updates:
        if is_update_valid(update, rules):
            total_middle_pages += find_middle_page(update)
    
    return total_middle_pages



with open("d5.txt", 'r') as file:
        input_text = file.read()
        
# Calculate the result
result = process_updates(input_text)
print(result)


##part 2
def reoder_update(update, rules):
    # Create a dictionary to map each page to its position
    #print(update)
    page_positions = {page: idx for idx, page in enumerate(update)}
    
    reo=True
    while(reo):
        # Check each rule and reorder 
        reo = False
        for X, Y in rules:
            if X in page_positions and Y in page_positions:  # Both pages must be in the update
                if page_positions[X] > page_positions[Y]:  # X must appear before Y
                    page_positions[X], page_positions[Y]=page_positions[Y], page_positions[X]
                    reo=True
  
    sorted_keys = [key for key, value in sorted(page_positions.items(), key=lambda x: x[1])]
    #print(sorted_keys)
    return sorted_keys

def process_updates_reorder(input_text):
    # Parse input
    rules, updates = parse_input(input_text)
    
    # Process each update and calculate the sum of middle pages
    total_middle_pages = 0
    for update in updates:
        if not(is_update_valid(update, rules)):
            total_middle_pages += find_middle_page(reoder_update(update, rules))
    
    return total_middle_pages

# Calculate the result
result = process_updates_reorder(input_text)
print(result)