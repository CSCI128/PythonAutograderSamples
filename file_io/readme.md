# File IO Autograder Example

This is a demonstration about how to create a file IO autograder with the autograder platform. 

This autograder builds off of the `basic_io` autograder, so I recommend being familiar with that one prior to reading 
through this autograder. 

File IO is completely independent of stdio / functions / ect. This means that file IO can be used in conjunction with 
any other features of the autograder with no extra configuration required.

## Problem

### Background

You have been tasked with creating a custom file parser for a proprietary file format at your new job.
This file format is similar to CSV but also contains metadata about each column in the file. The parser written here 
will be integrated into a larger system by another member of your team.


