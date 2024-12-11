# My Crazy Idea: Creating a New IP Addressing System

## Why I Don't Like IPv4?

The main issue with IPv4 is that not everyone has a **WHITE IP** (in short, if you have a white IP, you can host servers on the internet).

## What Am I Proposing?

A solution to all problems!

### What I Want to Do:

(You probably won't understand what I wrote)

Let me explain it to you. Imagine we have a device in the network without a white IP, let's call it the **client**. Now, imagine we have another device in the network with a white IP, let's call it the **retranslator**.

Each client will assign itself a retranslator through which it will receive messages.

### Example IP:

```
173.194.73.139:8080::OOMG
```

### What It Means:

```
IP Address of Retranslator | Port of Retranslator | Last 4 random chars
173.194.73.139             : 8080                 :: OOMG
```

### Scenario:

Imagine a client (with a grey IP) wants to receive data from another client (also with a grey IP). Here's what happens:

1. The first client contacts the retranslator of the second client.
2. The second client is already connected to the retranslator, so the second client receives the message from the retranslator.
3. The second client sends the requested data back to the retranslator.
4. The retranslator forwards this data to the first client.


# Protocol
[Protocol](protocol.md)

# Support Me

TON Network: UQBupVqXGQHoHhRfLYRqLFqhHt1KznRNiwRiifZWx_d5SKmG
