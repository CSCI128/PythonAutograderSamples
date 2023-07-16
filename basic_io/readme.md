# Basic IO Autograder Example

This autograder is a demonstration on how to do basic IO with the autograder platform.
This autograder uses both functions and code executed in `__main__`. For this autograder, return values
are not taken in consideration.

I recommend reading the `test_public_main.py` first to understand the general pipeline
that is needed for the autograder.


## Problem

### Background

You are in charge of inventory for a local grocery store. Part of your duties include updating the current inventory as 
shipments come in and customers purchase goods. You want to write a simple python script to tell you what the inventory 
of your store is after a full day of business.

### Requirements
You receive inventory changes in the following format
```text
<change_type>:<item>:<units>
```

For instance, if you received a shipment of 50 apples, the inventory change would be

```text
shipment:apples:50
```

If you sold 50 apples, the inventory change would be
```text
sale:apples:50
```

Write at least two functions, `record_shipment(item, amt)` and `record_sale(item, amt)` that print to the console the 
inventory change and update the store's stock.

For instance, the `record_shipment` function would print the following upon receiving 50 apples.
```text
OUTPUT Received shipment of 50 apples
```

The `record_sale` function would print the following upon selling 50 apples.

```text
OUTPUT Sold 50 apples
```

Your program should prompt you to enter inventory changes till you type EOD (end of day).

### Error Handling
If there is not enough inventory of the item in stock, then you should sell the remaining amount.

For instance:

```text
INPUT> shipment:apple:5
OUTPUT Received shipment of 5 apples
INPUT> sale:apples:6
OUTPUT Sold 5 apples
INPUT> EOD
OUTPUT apples: 0
```

If that item has not been entered in inventory then an error should be printed.

For instance:

```text
INPUT> shipment:bananas:5
INPUT> sale:apples:5
OUTPUT ERROR: apples not found in inventory
INPUT> EOD
OUTPUT bananas: 5
```


If no items have been entered in inventory, then the user should be informed at EOD.

For instance:

```text
INTPUT> EOD
OUTPUT No items in inventory
```


### Hints
- Dictionaries are very useful for this assignment.
- `my_dictonary.keys()` tells you what entries are in your dictionary

### 


