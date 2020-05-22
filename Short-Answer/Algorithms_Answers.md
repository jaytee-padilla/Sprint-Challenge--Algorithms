#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Constant O(n). As the size of the input increases, the runtime or space used will grow at the same rate. n remains the same value, only a's value if affected.


b) Polynomial O(n log n). The while loop nested in the for loop means 2 loops are happening for each element based on n's value.


c) Exponential O(n). The recursion triggers based on n (bunnies)

## Exercise II
1. Split the value of n in half
2. Starting from the middle point (n // 2) of n, drop the egg
3. If the egg breaks, split the current value of n (left hand side) in half again
4. If the egg breaks, continue splitting the current value of n in half and dropping the egg from that floor
5. If the egg doesn't break upon being dropped from a certain floor, loop from the current value of n to n * 2 & drop the egg each iteration to find the exact floor that the egg begins breaking.

I think the runtime complexity would be Logarithmic O(log n) because the value of n is being split in half each run through, therefore the runtime grow at a slightly slower rate as the size of the input increases

