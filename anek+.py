import time

def print_ascii_animation():
    frames = [
        r"""
      ___  
    ('v')/ 
    //-=-\\ 
    (\_=_/) 
   ^^ /^_\^^""",
        r"""
      ___  
    ('v')/ 
    //-=-\\ 
    (\_=_/) 
   ^^ /^_\^^""",
        r"""
      ___  
    ('v')/ 
    //-=-\\ 
    (\_=_/) 
   ^^ /^_\^^""",
        r"""
      ___  
    ('v')/ 
    //-=-\\ 
    (\_=_/) 
   ^^ /^_\^^""",
    ]

    for frame in frames:
        print("\033c", end="")
        print(frame)
        time.sleep(0.5)

print_ascii_animation()