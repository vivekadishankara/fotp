# fotp
Front Office Trading Platform

The github page can be found [here](https://github.com/vivekadishankara/fotp)

---
### User Guide
Clone the repository using the command:
```commandline
git clone git@github.com:vivekadishankara/fotp.git
```
Enter the folder and set up a virtual environment using the requirements
```commandline
cd fotp
python -m venv venv
pip install -Ur requirements.txt
```
Start the Event Manager by running the main.py file
```commandline
python main.py
```
Now you can send the request to fotp.
To do that save it in a file named 'request_{order_id}' in the communication/requests folder.
The reader reads the folder and loads new requests every 10 seconds. An example request has already been places in the
folder.
The corresponding responses will appear in the 'communication/responses' folder

A few rules are places in the 'rules' folder. You can modify them or add your own in the file.
The conditions to be met during the writing of a rule are as follows:
* It needs to be a single function
* It can only take one argument, that is an instance of Order
* It needs to send a list of ResponseTypes
```python
from typing import List
from application.trade.Order import Order
from application.trade.ArgTypes import ResponseType

def rule_127(order: Order) -> List[ResponseType]:
    """Logic to generate response types"""
    return [ResponseType.NEW_ORDER_CONFIRM]
```
---

### Developer's Guide
The file 'task_list.txt' holds the tasks to be implemented in the repository.
Tasks with a star '*' at the beginning have been completed.

You can pick up an uncompleted task from the tasklist.txt or add your own.