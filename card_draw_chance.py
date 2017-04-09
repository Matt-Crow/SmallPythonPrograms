def run():
  global starting_hand
  global num_copies
  global deck_size
  global draw_chance
  starting_hand = int(raw_input("Starting hand size: "))
  num_copies = float(raw_input("Number of copies: "))
  deck_size = float(raw_input("Deck size: "))
  draw_chance = 0.0
  test()
  run()

def draw():
  global draw_chance
  global deck_size
  draw_chance += num_copies / deck_size
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