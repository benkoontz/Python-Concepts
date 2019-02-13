# python prgram that reads and writes files
fw = open('sample.txt', 'w') # w is for writing
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r') # r is for reading
text = fr.read()
print(text)
fr.close()
