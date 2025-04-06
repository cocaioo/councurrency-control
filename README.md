# 🧵 Producer-Consumer with Threads in Python

This project is an implementation of the **classic Producer-Consumer problem** using Python's `threading` and `semaphores`, with optional **alternating execution** when there is exactly one producer and one consumer.

---

## 📌 Purpose

To simulate the production and consumption of items in a **bounded buffer**, ensuring proper synchronization between producer and consumer threads.

---

## ⚙️ How It Works

- **Producers** generate random numbers and insert them into a shared buffer.
- **Consumers** remove items from the buffer and "consume" them.
- The code ensures:
  - No insertion occurs when the buffer is full.
  - No removal occurs when the buffer is empty.
  - All buffer operations are thread-safe using a `mutex`.
  - When there is **exactly one producer and one consumer**, the system alternates strictly between producing and consuming for simplicity.

---

## 🧪 Features

- Fixed-size buffer using Python's `queue.Queue`.
- Configurable number of producers and consumers.
- Two execution modes:
  - **Alternating Mode**: When the number of producers equals the number of consumers and both are 1.
  - **Semaphore-Controlled Mode**: When producers and consumers operate independently using counting semaphores and locks.
- Random sleep intervals simulate variable processing times.

---

## 🛠️ Requirements

- Python 3.x

_No external libraries required._

---

## ▶️ Running the Code

To run the script:

```bash
python producer_consumer.py
