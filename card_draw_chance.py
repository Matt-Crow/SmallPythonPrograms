def int_input(msg):
  inp = raw_input(msg)
  try:
    inp = int(inp)
    if inp <= 0:
      print("Please enter a non-negative number")
      int_input(msg)
    else:
      return inp
  
  except:
    print("Please enter a valid non-decimal number")
    int_input(msg)

def run():
  global starting_hand
  global num_copies
  global deck_size
  global draw_chance
  global not_draw
  
  starting_hand = int_input("Starting hand size: ")
  num_copies = int_input("Number of copies: ")
  
  deck_size = 0
  while num_copies > deck_size:
    deck_size = int_input("Deck size: ")
  
  draw_chance = 0.0
  not_draw = 1.0;
  test()
  cont = raw_input("Do you wish to continue? y/n")
  if cont == "y":
    run()

def draw():
  global draw_chance
  global not_draw
  global deck_size
  
  not_draw *= float((deck_size - num_copies)) / deck_size
  draw_chance = 1.0 - not_draw
  
  if draw_chance >= 1.0:
  	draw_chance = 1.0
  
  deck_size -= 1
  
def draw_start():
  drawn = 0
  while drawn < starting_hand:
    draw()
    drawn += 1
    
def test():
  print(" ")
  print("The chance of drawing a card from a deck of " + str(int(deck_size)) + " cards")
  print("given " + str(int(num_copies)) + " copies")
  print("in a starting hand of " + str(starting_hand) + " cards is:")
  draw_start()
  print(str(int(draw_chance * 100)) + "%")
  print(" ")

run()