*Python Multiprocessing Examples*
This collection demonstrates how to use Python's multiprocessing module to run the same simple task—summing numbers from 0 to 999,999—in various ways.

Codes details:
Basic Process Spawn
Runs multiple processes, each computing the sum and printing its result.

Named vs Default Processes
Shows how custom process names affect output and helps track running processes.

Daemon vs Non-Daemon Processes
Illustrates background (daemon) processes and normal (non-daemon) processes running the sum task.

Subclassing Process
Creates a custom process class by extending multiprocessing.Process, running the summation inside.

Producer-Consumer Pattern
Implements a classic queue-based producer-consumer problem with two separate processes communicating via a queue.

Why Use These?
Learn different ways to run parallel CPU-bound tasks.

Understand process lifecycle, names, and daemon behavior.

See how subclassing can customize process execution.

Explore safe communication between processes using queues.

How to Run
Run each script independently in a Python 3 environment, e.g.:
python basic_process_spawn.py

Watch how each process calculates and outputs results concurrently. Ideal for anyone learning Python parallel programming practicalities.
