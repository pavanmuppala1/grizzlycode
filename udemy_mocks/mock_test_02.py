try:
  val = int(input('provide a number: '))
  print(val/val)
except TypeError:
  print('a')
except ValueError:
  print('b')
except ZeroDivisionError:
  print('c')
except:
  print('d')