# Consistent Hashing — Voice-over Script

Voice: Microsoft Ravi (English, India)

## 1. Introduction

Consistent hashing is a technique used in distributed systems to spread data across multiple servers. Imagine many users sending requests to a single server. As traffic grows, that server becomes overloaded, creating slow responses and a single point of failure. We need a way to distribute both requests and stored data efficiently, while still knowing exactly where each item belongs. That is the problem consistent hashing helps us solve.

## 2. Scaling the system

As the number of users increases, one server can no longer handle the complete load. We can add more servers, but this creates an important question: which server should store a particular key, such as Alice, Bob, Charlie, or David? Every client must follow the same predictable rule. The rule should distribute data evenly, find data quickly, and continue working when servers are added or removed.

## 3. Traditional hashing

A simple approach is traditional modulo hashing. First, convert each key into a numeric hash. Then take that value modulo the number of servers. With three servers, Alice's hash of one hundred fifty-four maps to server one. Bob maps to server zero, Charlie to server two, and David to server zero. This works until capacity changes. When a fourth server is added, the formula changes from modulo three to modulo four. Most keys now produce a different result. In this example, three out of four keys move, causing expensive data transfers and many cache misses.

## 4. The hash ring

Consistent hashing changes the shape of the hash space. Instead of treating it as a straight line, we wrap the end back to the beginning, forming a circle called the hash ring. Here the values run from zero through one thousand twenty-three, and after the final value we return to zero. Both servers and data keys will be hashed into positions on this same ring. Searches move around it in the clockwise direction.

## 5. Placing servers

We begin by hashing each server identifier. Server A lands at position one hundred twenty, server B at four hundred twenty, and server C at eight hundred ten. A server owns the range immediately before its position, up to and including its own point on the ring. The colored arcs show these ownership ranges. Notice that the ranges are not necessarily equal, because normal hash values are distributed randomly. Next, we will place the data keys into this same circular space.

## 6. Placing keys

Each data key is passed through the same hash function. Apple lands at two hundred ten, Banana at five hundred sixty, Mango at seven hundred thirty, and Orange at nine hundred twenty. At this stage, the dots only show hash positions; the keys have not yet been assigned to servers. To determine ownership, start at a key and move clockwise around the ring. The first server reached becomes the owner of that key.

## 7. Clockwise lookup

Now let us apply the lookup rule. Apple is at two hundred ten. Moving clockwise, the first server is B, so B stores Apple. Banana is at five hundred sixty, and the first server clockwise is C. Orange is at nine hundred twenty. Moving forward wraps around past zero, making server A its owner. Mango, at seven hundred thirty, also reaches server C first. The rule is always identical: begin at the key's hash position and move clockwise until the first server is found. This simple rule gives every key one deterministic owner.

## 8. Adding a server

Suppose we add server D at hash position six hundred twenty. Before the change, the existing servers own their colored regions and all keys follow the clockwise rule. After D joins the ring, it takes only the interval immediately before its new position. Banana falls inside this interval, so its ownership changes from server C to server D. The other keys stay where they are. This is the central advantage of consistent hashing: adding capacity moves only a small, local portion of the data rather than remapping almost every key.

## 9. Removing a server

The same local behavior applies when a server is removed or fails. Here server B leaves the ring. Only the keys that were owned by B need to be reassigned. Each affected key continues clockwise and moves to the next available server. Keys belonging to A, C, or D remain unchanged. Because failures affect only a limited interval, recovery requires much less data movement than modulo hashing and the rest of the system can continue operating normally.

## 10. Virtual nodes

There is still one practical issue. With only one position per physical server, randomly sized ownership regions can create an uneven load. Virtual nodes solve this by placing each physical server at several positions around the ring. The virtual nodes for A, B, and C are spread throughout the hash space, and every virtual node points back to its physical server. Many smaller regions are therefore mixed across the ring. As more keys are added, the load becomes much more balanced. Virtual nodes also make capacity weighting easier and reduce the impact of a single server failure, while preserving minimal data movement.

## 11. Replication

Distributed storage also needs protection against failure. For each key, the first server clockwise stores the primary copy. Additional copies are placed on the next distinct servers around the ring. In this example, every key has one primary and two replicas. If the primary server becomes unavailable, another server can still serve the data. Replication improves high availability, fault tolerance, and durability. In a real system, the replication factor can be adjusted to balance reliability, storage cost, and consistency requirements.

## 12. Summary

In summary, consistent hashing places servers and keys on a ring, finds owners clockwise, and limits remapping when membership changes. Virtual nodes balance the load, while replication protects the data. The result is a scalable, fault-tolerant system with minimal key movement. Thank you.
