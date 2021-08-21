from tkinter import *

root=Tk()

def evolution():
    #global state256, state128, state64, state32, state16, state8, state4, state2, state1
    state256 = cell256_text.get()
    state128 =cell128_text.get()
    state64 =cell64_text.get()
    state32 =cell32_text.get()
    state16 =cell16_text.get()
    state8 =cell8_text.get()
    state4 =cell4_text.get()
    state2 =cell2_text.get()
    state1 =cell1_text.get()
    cell256 = int(state128) + int(state32) + int(state16)
    if cell256 == 3:
        cell256_text.delete(0, END)
        cell256_text.insert(0, "1")
    elif cell256 > 3 or cell256 <2:
        cell256_text.delete(0, END)
        cell256_text.insert(0, "0")

    cell128 = int(state256) + int(state64) + int(state32) + int(state16) + int(state8)
    if cell128 == 3:
        cell128_text.delete(0, END)
        cell128_text.insert(0, "1")
    elif cell128 > 3 or cell128 <2:
        cell128_text.delete(0, END)
        cell128_text.insert(0, "0")

    cell64 = int(state128) + int(state16) + int(state8)
    if cell64 == 3:
        cell64_text.delete(0, END)
        cell64_text.insert(0, "1")
    elif cell64 > 3 or cell64 <2:
        cell64_text.delete(0, END)
        cell64_text.insert(0, "0")

    cell32 = int(state256) + int(state128) + int(state16) + int(state4) + int(state2)
    if cell32 == 3:
        cell32_text.delete(0, END)
        cell32_text.insert(0, "1")
    elif cell32 > 3 or cell32 <2:
        cell32_text.delete(0, END)
        cell32_text.insert(0, "0")

    cell16 = int(state256) + int(state128) + int(state64) + int(state32) + int(state8) + int(state4) + int(state2) + int(state1)
    if cell16 == 3:
        cell16_text.delete(0, END)
        cell16_text.insert(0, "1")
    elif cell16 > 3 or cell16 <2:
        cell16_text.delete(0, END)
        cell16_text.insert(0, "0")

    cell8 = int(state128) + int(state64) + int(state16) + int(state2) + int(state1)
    if cell8 == 3:
        cell8_text.delete(0, END)
        cell8_text.insert(0, "1")
    elif cell8 > 3 or cell8 <2:
        cell8_text.delete(0, END)
        cell8_text.insert(0, "0")

    cell4 = int(state32) + int(state16) + int(state2)
    if cell4 == 3:
        cell4_text.delete(0, END)
        cell4_text.insert(0, "1")
    elif cell4 > 3 or cell4 <2:
        cell4_text.delete(0, END)
        cell4_text.insert(0, "0")

    cell2 = int(state32) + int(state16) + int(state8) + int(state4) + int(state1)
    if cell2 == 3:
        cell2_text.delete(0, END)
        cell2_text.insert(0, "1")
    elif cell2 > 3 or cell2 <2:
        cell2_text.delete(0, END)
        cell2_text.insert(0, "0")

    cell1 = int(state16) + int(state8) + int(state2)
    if cell1 == 3:
        cell1_text.delete(0, END)
        cell1_text.insert(0, "1")
    elif cell1 > 3 or cell1 <2:
        cell1_text.delete(0, END)
        cell1_text.insert(0, "0")

def getBinary():
    state256 = cell256_text.get()
    state128 =cell128_text.get()
    state64 =cell64_text.get()
    state32 =cell32_text.get()
    state16 =cell16_text.get()
    state8 =cell8_text.get()
    state4 =cell4_text.get()
    state2 =cell2_text.get()
    state1 =cell1_text.get()
    displayBinary.delete(0,END)
    displayBinary.insert(0, str((int(state256)*256)+(int(state128)*128)+(int(state64)*64)+(int(state32)*32)+(int(state16)*16)+(int(state8)*8)+(int(state4)*4)+(int(state2)*2)+(int(state1)*1)))

def binaryMapping():
    map = displayBinary.get()
    map256 = (int(map)&256)/256
    map128 = (int(map)&128)/128
    map64 = (int(map)&64)/64
    map32 = (int(map)&32)/32
    map16 = (int(map)&16)/16
    map8 = (int(map)&8)/8
    map4 = (int(map)&4)/4
    map2 = (int(map)&2)/2
    map1 = int(map)&1
    cell256_text.delete(0, END)
    cell128_text.delete(0, END)
    cell64_text.delete(0, END)
    cell32_text.delete(0, END)
    cell16_text.delete(0, END)
    cell8_text.delete(0, END)
    cell4_text.delete(0, END)
    cell2_text.delete(0, END)
    cell1_text.delete(0, END)
    cell256_text.insert(0, int(map256))
    cell128_text.insert(0, int(map128))
    cell64_text.insert(0, int(map64))
    cell32_text.insert(0, int(map32))
    cell16_text.insert(0, int(map16))
    cell8_text.insert(0, int(map8))
    cell4_text.insert(0, int(map4))
    cell2_text.insert(0, int(map2))
    cell1_text.insert(0, int(map1))
    
def automatedEvo():
    binaryMapping()
    for x in range(15):
        evolution()
    getBinary()

def simulateAllCombinations():
    seed = int(0)
    file = open("Evolution Combination.txt", "a")
    file.write("Initial State   Number of Generations   Final State\n")
    file.close()
    while seed < 512:
        displayBinary.insert(0, seed)
        binaryMapping()
        generations = 0
        prev = 0
        for x in range(15):

            evolution()
            getBinary()
            if prev != displayBinary.get():
                generations=generations+1
                prev=displayBinary.get()

        file = open("Evolution Combination.txt", "a")
        file.write(str(seed) + "                       " + str(generations) + "                    " + displayBinary.get() + "\n")
        file.close()
        seed= seed+1
        displayBinary.delete(0, END)
    

cell256_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100,), justify='center')
cell128_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100), justify='center')
cell64_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100), justify='center')
cell32_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100), justify='center')
cell16_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100), justify='center')
cell8_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100), justify='center')
cell4_text = Entry(root, width=3,  borderwidth=5, font=("Times New Roman", 100), justify='center')
cell2_text = Entry(root, width=3, borderwidth=5, font=("Times New Roman", 100), justify='center')
cell1_text = Entry(root, width=3, borderwidth=5, font=("Times New Roman", 100), justify='center')

displayBinary = Entry(root, width=10, borderwidth=5, font=("Times New Roman", 100))

evolve = Button(root, text="EVOLVE!!!", padx=10, pady= 1, font=(200),command=lambda: evolution())
binaryValue = Button(root, text="Get Binary Value", padx=10, pady= 1, font=(200),command=lambda: getBinary())
useBinaryMap = Button(root, text="Use Binary Value as Map", padx=10, pady= 1, font=(200),command=lambda: binaryMapping())
automate = Button(root, text="Automate the Evolution", padx=10, pady= 1, font=(200),command=lambda: automatedEvo())
simulateAll = Button(root, text="SIMULATE ALL POSSIBLE COMBINATION!!!", padx=10, pady= 1, font=(200),command=lambda: simulateAllCombinations())

displayBinary.grid(row=0, column=0, columnspan=3)
cell256_text.grid(row=1, column=0)
cell128_text.grid(row=1, column=1)
cell64_text.grid(row=1, column=2)
cell32_text.grid(row=2, column=0)
cell16_text.grid(row=2, column=1)
cell8_text.grid(row=2, column=2)
cell4_text.grid(row=3, column=0)
cell2_text.grid(row=3, column=1)
cell1_text.grid(row=3, column=2)
evolve.grid(row=4, column=0, columnspan=3)
binaryValue.grid(row=5, column=0, columnspan=3)
useBinaryMap.grid(row=6, column=0, columnspan=3)
automate.grid(row=7, column=0, columnspan=3)
simulateAll.grid(row=8, column=0, columnspan=3)



root.mainloop()