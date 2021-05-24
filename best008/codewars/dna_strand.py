def DNA_strand(dna):
    dict_DNA = {"A":"T",
                "T":"A",
                "C":"G",
                "G":"C"} 
    return [dict_DNA[i] for i in dna if i in dict_DNA.keys()]

    # code here

print(* DNA_strand ("ATTGC")) # return "TAACG"
print(* DNA_strand ("GTAT")) # return "CATA"