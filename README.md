# SmashingLab
An exploit that uses a stack overflow to delete a file named target.txt from a thttpd server. Converting NOpexploit.txt or exp.txt into a raw file (after removing the newlines added for required specifications), and running the server with the raw file as the input for the -C option will cause target.txt to be deleted from the current directory. 

The development of this exploit is described in smashinglab.txt, beginning at bullet point 9. NOPexploit.txt uses NOP sleds to allow for greater variation in stack memory addresses, while exp.txt simply overwrites the expected address for the return address. Note that this exploit was designed to work when stack protection is disabled.
