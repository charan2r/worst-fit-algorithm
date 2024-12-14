# class to manage individual memory blocks
class MemoryBlock:
    def __init__(self, size, index):
        self.size = size
        self.index = index

    def allocate(self, process_size):
        if process_size <= self.size:
            self.size -= process_size
            return True
        return False

# class to manage processes with sizes
class Process:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.allocated_block = None

# class to manage memory allocation
class WorstFitAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = [MemoryBlock(size, i + 1) for i, size in enumerate(memory_blocks)]

    def allocate_process(self, process):
        # Find the largest block that can fit the process
        worst_block = None
        for block in self.memory_blocks:
            if block.size >= process.size and (worst_block is None or block.size > worst_block.size):
                worst_block = block

        # Allocate memory if a suitable block is found
        if worst_block and worst_block.allocate(process.size):
            process.allocated_block = worst_block.index

    def allocate_processes(self, processes):
        for process in processes:
            self.allocate_process(process)

    def get_memory_state(self):
        return [(block.index, block.size) for block in self.memory_blocks]

# Initial memory state (in KB)
memory_block_sizes = [200, 300, 400, 100, 150]

# Processes to be allocated
processes = [
    Process("Process A", 120),
    Process("Process B", 250),
    Process("Process C", 50)
]

# Allocate memory using Worst Fit algorithm
allocator = WorstFitAllocator(memory_block_sizes)
allocator.allocate_processes(processes)

# Display the results
print("Allocation Results:")
for process in processes:
    if process.allocated_block:
        print(f"{process.name} is allocated to Block {process.allocated_block}.")
    else:
        print(f"{process.name} could not be allocated.")

print("\nUpdated Memory Blocks:")
for block_index, size in allocator.get_memory_state():
    print(f"Block {block_index}: {size} KB")
