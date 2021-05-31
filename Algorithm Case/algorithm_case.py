INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(input):

  # input splited from string to list
  input = input.split(" ")
  output=""
  
  # loop over the input's words because of we have to fixed reverse order words and clean paranthessis
  for i in input:
    # if word reverse order then enter if statement and reverse word to correct result
    if(i[0] != "(" and i[-1] != ")"):
      
      # reversed word
      i = i[::-1]

      # this statement for first word in the sentences
      if(len(output) == 0 ):
        output = output + i
        
      # if word not first word in sentence then add the output string with space among two word
      else:
        output = output + " " + i
    
    # if word correct order then control the paranthessis and clean it
    else:
      # if word start with (  and end with ) clean that paranthessis
      if((i[0] == "(" and i[1] == "(")):
        i = i.replace("(", "", 1)
        i = i.replace(")", "")
        output = output + " " + i

      # if word have any paranthessis clean it all
      else:
        i = i.replace("(", "")
        i = i.replace(")", "")
        output = output + " " + i

  print(output)
  print(CORRECT_ANSWER)
  return output

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")

