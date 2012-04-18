import random
import sys
import optparse

class OneTimePad:
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		with open("dropbox/msg.txt", 'r') as data:
			self.msg = data.read()
			data.close()

	def encrypt (self):
		""" Our encryption function. """
		key = []
		offset = []
		secret_message = []
		
		for i in range(len(self.msg)):
			key.append(random.randint(1,52))
			offset.append(ord(self.msg[i])+key[-1])
			secret_message.append(chr(offset[i]))
			key[i] = str(key[i])
			
		for i, element in enumerate(key):
			if int(key[i]) < 10:
				key[i] = '0'+key[i]
				
		key = ''.join(key)
		secret_message = ''.join(secret_message)
		
		with open("dropbox/key.txt", 'w') as data:
			data.write(key)
			data.close()
		with open("dropbox/secret_msg.txt", 'w') as data:
			data.write(secret_message)
			data.close()
			
	def decrypt (self):
		""" Decrypt our secret message """
		with open("dropbox/secret_msg.txt", 'r') as data:
			secret_message = data.read()
			data.close()
		with open("dropbox/key.txt", 'r') as data:
			key = data.read()
			data.close()
		
		key_values = []
		true_message = []
		i = 0
		
		while i < len(key):
			temp = '{}{}'.format(key[i],key[i+1]) 
			key_values.append(int(temp))
			i+= 2
			
		for i in range(len(secret_message)-1):
			true_message.append(ord(secret_message[i])-key_values[i])
			true_message[i] = chr(true_message[i])
		
		true_message = ''.join(true_message)
		with open("dropbox/new_msg.txt", 'w') as data:
			data.write(true_message)
			data.close()
		
		
if __name__ == '__main__':
	
	parser = optparse.OptionParser()
	
	parser.add_option('-e',
					  '--encrypt',
					  dest = 'encrypt',
					  default = False,
					  type ='int',
					  help ='Arg of 1 will encrypt the file in drop box')
					  
	parser.add_option('-d',
					  '--decrypt',
					  dest ='decrypt',
					  default = False,
					  type ='int',
					  help ='Arg of 1 will decrypt the file in drop box')
					  
	(options, args) = parser.parse_args()
	if len(sys.argv) < 1:
		parse.error('Incorrect number of arguments. See help -h')
	if options.encrypt == 1:
		OneTimePad().encrypt()
	if options.decrypt == 1:
		OneTimePad().decrypt()
