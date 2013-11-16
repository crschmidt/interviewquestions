# This solution is just an implementation of 
# http://stackoverflow.com/a/15722968/281837 in Python; I can take no credit
# for the cleverness here.

# Fatal flaw; doesn't actually enforce integer division rules, so it produces
# values where "2/5" is treated as '0' when instead it should be treated as
# an illegal operation; because of 'cheating' and putting hte operator string
# into the list instead of the result value, there isn't a trivial solution
# to check that error case.

def search(numbers, target, progress_so_far=None, target_size = None):
    if not target_size:
        target_size = len(numbers)
    if not progress_so_far:
        progress_so_far = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for op in ['+', '-', '*', '/']:
                op_string = "%s%s%s" % (numbers[i], op, numbers[j])
                try:
                    result = eval(op_string)
                except:
                    continue
                    
                if result == target and target_size == (progress_so_far+2):
                   print "solution", numbers[i], op, numbers[j], "= %s" % target
                elif len(numbers)>2:
                    new_numbers = list(numbers)
                    new_numbers.remove(numbers[i])
                    new_numbers.remove(numbers[j])
                    new_numbers.append(op_string)
                    search(new_numbers,target, progress_so_far+1,target_size)

#search([1,2,3], 0) 
 
search([1,2,3,4,5,6], 73) 
