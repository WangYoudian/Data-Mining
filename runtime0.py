from pymining import assocrules, perftesting, itemmining, perftesting, seqmining
import time
import sys



'''
Options:
1.Frequent Item Set Mining
2.Association Rules Mining
3.Frequent Sequence Mining
'''
def func(case):
	#switcher = {}   python don't have an equivalent to 'switch'
	if case == '1':
		fun1()
	elif case == '2':
		fun2()
	elif case == '3':
		fun3()
	elif case == '4':
		fun4()
	elif case == '5':
		sys.exit()
	else:
		print("We are sorry but you gave the wrong input, Pls reinput")
		case = input()
		func(case)


def content():
	print("\n")
	time.sleep(0.5)
	print("Content:\n1.Frequent Item Set Mining\n2.Association Rules Mining\n3.Frequent Sequence Mining\n4.Testing efficiency of three different mining algorithms\n5.exit")
	chc = input("We offer several mining tools, choose the number you want to enter\n")
	func(chc)
	content()

# Frequent Item Set Mining
def fun1():
	transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
	relim_input = itemmining.get_relim_input(transactions)
	report = itemmining.relim(relim_input, min_support = 2)
	print("Here is the default transactions data.\n{}".format(transactions))

	time.sleep(0.5)
	print("See the default frequent itemsets?[y/n]")
	p1 = input() 
	if p1 == 'y':
		print(report)
		input("Press any button to return to CONTENT")
	else:
		input("Thank you for visiting, press Any button to return to CONTENT")

# Association Rules Mining
def fun2():
	transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
	relim_input = itemmining.get_relim_input(transactions)
	item_sets = itemmining.relim(relim_input, min_support = 2)
	rules = assocrules.mine_assoc_rules(item_sets, min_support =2, min_confidence = 0.5)
	print("The default transactions data is:")
	print(transactions)

	time.sleep(0.5)
	input("Press any button to continue...")
	print("Here is the association rules we have mined. Frozenset means the pattern in the transactions")
	time.sleep(1)
	print(rules)
	print("\nNote:(frozenset({e'}), frozenset({'b', 'd'}), 2, 1.0) means:\n # e -> b, d with support 2 and confidence 0.66")
	input("Press Any button to return to CONTENT")

# Frequent Sequence Mining
def fun3():
	seqs = ('caabc', 'abcb', 'cabc', 'abbca')
	freq_seqs = seqmining.freq_seq_enum(seqs, 2)
	print("The default sequence data is:")
	print(seqs)

	time.sleep(1)
	input("Press any key to see the discovered frequent seqences")
	print(sorted(freq_seqs))
	print("\nNote:(('a', 'b'), 4) means:\nIn the given seqs tuple, there are 4 times that 'b' appears after 'a'")
	input("Press Any button to return to CONTENT")

def fun4():
	perftesting.test_itemset_perf()
	print("\nAs you can see, Relim is the best performing algorithm!\n")
	input("Press Any button to return to CONTENT")


if __name__ == '__main__':
	content();
