radif, cheir_number = input().split()
radif, cheir_number = int(radif), int(cheir_number)
left_right = "Left" if cheir_number > 10 else "Right"
radifGO = 11-radif
cheir_numberGO = cheir_number if left_right == "Right" else 21-cheir_number
print(left_right, radifGO, cheir_numberGO)
