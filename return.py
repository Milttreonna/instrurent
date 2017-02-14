
      if "clarinet" in whatInstrument:
          dict['Clarinet'] = int(dict["Clarinet"]) + 1

      elif "piano" in whatInstrument:
          dict['Piano'] = int(dict["Piano"]) + 1

      elif "violin" in whatInstrument:
          dict['Violin'] = int(dict["Violin"]) + 1

      elif "electric" in whatInstrument or whatInstrument == "electricguitar":
          dict['Electric-guitar'] = int(dict["Electric-guitar"]) + 1

      elif "acoustic" in whatInstrument or whatInstrument == "acousticguitar":
          dict['Acoustic-guitar'] = int(dict["Acoustic-guitar"]) + 1

      elif "banjo" in whatInstrument:
          dict['Banjo'] = int(dict["Banjo"]) + 1

      elif "trumpet" in whatInstrument:
          dict['Trumpet'] = int(dict["Trumpet"]) - 1

      elif "saxophone" in whatInstrument:
          dict['Saxophone'] = int(dict["Saxophone"]) - 1

      elif "conga" in whatInstrument:
          dict['Conga-set'] = int(dict["Conga-set"]) - 1

      elif "drum" in whatInstrument:
          dict['Drum-set'] = int(dict["Drum-set"]) - 1

      elif whatInstrument == "q":
          print("Canceling. . .")
          sys.exit()
      else:
          print("Invalid answer")
          return itemInfo()
