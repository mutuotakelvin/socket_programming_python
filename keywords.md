### Aim of creating a UDP SERVER
- Print the original message received from the client.
- Capitalize the message.
- Send the capitalized version back to the client.
---------------------------------------------------
--getsockname() - used on a socket object to find the current IP address and port that a socket is bound.

--Infinitely lstening- setting a while loop so that the server listens infinitely. else, the server would exit after dealing with one client.

--recvfrom() - this method accepts data of MAX_SIZE_BYTES length which is the size of one UDP datagram in bytes. 

-- decode the message from the byte stream to ASCII then capitalize it.

--sendto() - form sending back the message to client.