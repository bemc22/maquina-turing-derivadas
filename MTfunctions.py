import sys
from IPython.display import clear_output

#convert reading direction to index number
#r:right , l:left , s:stop
def dir2index(rdir):
	if rdir=="r":
		return 1
	elif rdir=="l":
		return -1
	elif rdir == "s":
		return 0


def validate(tapes,numTapes,myInput,input_symbols,states,transitions,initial_state,final_states):

	#Creates a given number of tapes
	for i in range(numTapes):
		tapes.append([""])
	for i in range(numTapes):
		if i!=0:
			#print("2nd and so on")
			numcells = 666
			for n in range(numcells):
				tapes[i].append("")
	print("Creating "+str(numTapes)+" tapes.\n")


	print("Reading input...")
	for i in myInput:
		tapes[0].append(i)
	tapes[0].append("")
	print("tape1:",tapes[0])
	print("tape2:",tapes[1])


	print("\nValidating input...")
	for m in myInput:
		if m not in input_symbols:
			print("Error: the letter "+m+" is not defined inside current input_symbols.\n")
			return 0


	print("Validating states...")
	for s in states:
		if s not in transitions:
			print("Error: there is not a transition entry for state ", s)
			print("All states must have a transition entry.\n")
			return 0


	#All tapes must start with index number 1
	indextapes=[]
	for t in range(numTapes):
		indextapes.append(1)


	print("\nProcessing...")
	head2 = initial_state

	while head2 not in final_states:
		try:
			print(transitions[head2][(tapes[0][indextapes[0]],tapes[1][indextapes[1]])])
			temp0 = transitions[head2][(tapes[0][indextapes[0]],tapes[1][indextapes[1]])]
		except:
			print("ERROR: there is not a transition for ",(tapes[0][indextapes[0]],tapes[1][indextapes[1]]))
			return 0

		for i in range(numTapes):
			#According to transition entries, letters for each tape position are updated
			tapes[i][indextapes[i]] = temp0[1][i]
			print(tapes[i])
			print("move-to: ",temp0[2][i],dir2index(temp0[2][i]))
			#According to transition entries, target index numbers are updated
			indextapes[i] = indextapes[i] + dir2index(temp0[2][i])
			print("new-pos: ",indextapes[i])
		#According to transition entries, target state is updated
		print("Next-state: "+temp0[0]+"\n")
		head2 = temp0[0]
        
	clear_output()
	print("\n-----------------------------------")
	print("Good!, the input word is accepted!")
	print("-----------------------------------")
	return tapes[1]
