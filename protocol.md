# Hosting

We have an **IP Relay**:

- **173.194.73.139:8754**

1. Connect to it via **Sockets**.
2. The relay should send us **"IPvDIY System"**. If this is the case, we proceed!
3. Next, we need to send in bytes:

- **```CONNECT@_SPEC_@DESIRED_ID```**

```@_SPEC_@``` - This is a delimiter string!

```DESIRED_ID``` - These are the last 4 characters of the IP that the server **might** assign to us.

4. The server should return:

- **```OK ID```**

ID - This is the ID used in the IP. For example, we were assigned OOMG.

So our IP is:

- **```173.194.73.139:8754::OOMG```**

5. Next, we simply **wait** for clients to contact us.
6. When clients contact us, the server will send the information that the client sent to us. The server **must** respond to it. The format of receiving and responding depends on the **protocol you are using**.

# Receiving Information
We have the **client's IP**:

- **173.194.73.139:8754::OOMG**

1. Take what is before ```::``` in the IP address:

- **173.194.73.139:8754**

2. Connect to this IP.
3. The server should send us **"IPvDIY System"**. If this is the case, we proceed!
4. The format for sending a request:

- **```SEND@_SPEC_@ID@_SPEC_@DATA@_SPEC_@```**

ID - This is what comes after :: in the IP.

DATA - The data we are sending.

5. The server should return a response to our request containing our precious data!
