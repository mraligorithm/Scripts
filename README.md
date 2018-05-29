# Monitoring
**IBM**
Question
Imagine that you are creating a monitoring solution for your service. What characteristics, key performance indicators, or output would you consider in determining the availability of the service to your end clients?
Answer:

- - - -
**IBM**
Parse a file containing multiple groups of IP addresses and print out only the group of IP addresses that match the label "Houston" which should be hard coded in your function for this particular exercise. The group name will be on its own line and will be unique in the input file. Each IP address will be on its own line in the input file. The file can contain blank lines. The function should output the IP addresses comma separated. Input: A sample inventory file which may contain various text and comments along with valid and invalid IP addresses. For example: [Dallas] 10.20.30.40 10.20.30.41 10.40.20.1 [Houston] 9.20.30.5 9.30.4.10 [Seattle] 172.10.2.35 Output: The list of IP addresses separated by commas. With "Houston" hard coded as the label, the output of the above example should be:\ 9.20.30.5,9.30.4.10


Often there is a need to run a task across a set of machines. The list of IP addresses for these machines could come from different sources and therefore be in different formats. Starting with a file that contains mainly IP addresses, one per line, your task is to write a function that converts the list of IP addresses into a comma separated list of IP address, ignoring any line that starts with a # and ignoring any line that does not contain a valid IP address. Input: A sample inventory file which may contain various text and comments along with valid and invalid IP addresses. For example: [zone1] 10.171.102.174 #10.171.102.195 10.171.102.182 [zone2] 10.171.3.172 10.171.3.21 #10.171.3.224 Output: The list of IP addresses separated by commas. For the above example, that would be: 10.171.102.174,10.171.102.182,10.171.3.172,10.171.3.21
- - - -

**IBM**
Using the Fibonacci sequence, print out a lower case letter (from the English alphabet) the number of times of the Fibonacci number in the corresponding index. A number in the Fibonacci sequence is calculated by: n[x-2] + n[x-1] = n[x] The sequence starts with n[1] = 1 and n[2] = 1. The index begins at 1, not 0. Be careful of off by 1 errors. You do not have to worry about exceeding the English alphabet s max index of 26. Example: Input: 5 Letter = e Fibonacci number n[5] = 5 Output: eeee Input: A single integer. Output: A number of lower case letters as described above.
 
#linux/Interview/monitoring
