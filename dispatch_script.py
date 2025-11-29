import os;

# input n amount of orders
# output n amount of order data and print data pairs
"""
<Host2KiSoft messageID="151">
<OrderData orderNumber="KNAPP_NO_LBA" sheetNumber="1">
<OrderType>15</OrderType>
<LoadUnitCode>01005957</LoadUnitCode>
<LoadCarrier>NE1</LoadCarrier>
<DispatchRampNumbers>
<DispatchRampNumber>116</DispatchRampNumber>
</DispatchRampNumbers>
<ControlParameters>
<ControlParameter>1</ControlParameter>
</ControlParameters>
</OrderData>
</Host2KiSoft>

<Host2KiSoft messageID="150">
<PrintDataMessage orderNumber="KNAPP_NO_LBA">
<DispatchRampNumbers>
<DispatchRampNumber>116</DispatchRampNumber>
</DispatchRampNumbers>
<ControlParameters>
<ControlParameter>9003</ControlParameter>
</ControlParameters>
<CheckCode>11110000642114410302</CheckCode>
</PrintDataMessage>
</Host2KiSoft>
"""

# def input_dispatch_order_params():
orderAmount = 0;
orderNumber = "";

starting_load_unit_code = 0;
filepath = 'generated_dispatch_orders.txt';
defualt_filepath = 'generated_dispatch_orders.txt';

count = 1;

while(os.path.exists(filepath)): 
    count += 1;
    file_parts = defualt_filepath.split(".");
    print(file_parts);
    filepath = file_parts[0] + "_0" + str(count) + "." + file_parts[1];
    print(f'filepath to write to: {filepath}');

print("Enter number of orders you would like to generate:")
while True:
    try: 
        orderAmount = int(input());
        if 0 < orderAmount <= 500:
            break;
        else:
            raise ValueError;
    except ValueError:
        print("Invalid input, enter a number 1-500 for order amount:");

print('Enter starting order number e.g. "KNAPP_ORDER":')
while True:
    try:
        orderNumber = input();
        if(len(orderNumber) >= 5 and orderNumber.replace('_', '').isalpha()):
            break;
        else:
            raise ValueError;
    except ValueError:
        print("Invalid order number, order number must be at least 5 ALPHABETIC characters:");
        

print('Enter starting 8 digit load unit code:')
while True:
    try:
        starting_load_unit_code = int(input());
        if (00000000 < starting_load_unit_code <= 99999999) and (len(str(starting_load_unit_code)) == 8):
            break;
        else:
            raise ValueError;
    except ValueError:
        print("Invalid input, enter valid 8 digit starting load unit code:");

print(f'Generating {orderAmount} orders with starting order number "{orderNumber}" and load unit code "{starting_load_unit_code}"...')

startOrderNumber = orderNumber;
load_unit_code = starting_load_unit_code;
for i in range(orderAmount):
    if(i > 9):
        orderNumber = startOrderNumber + "_" + str(i + 1);
    else:
        orderNumber = startOrderNumber + "_0" + str(i + 1);
    load_unit_code = starting_load_unit_code + i;
    print(f'generated order {i + 1}');
    print(f'order number now: {orderNumber}');
    print(f'load unit code: {load_unit_code}');

def write_dispatch_orders(filepath):
    order_data = [
        '<Host2KiSoft messageID="151">',
        f'<OrderData orderNumber={orderNumber} sheetNumber="1">',
        '<OrderType>15</OrderType>',
        f'<LoadUnitCode>{load_unit_code}</LoadUnitCode>',
        '<DispatchRampNumbers>',
        '<DispatchRampNumber>114</DispatchRampNumber>',
        '</DispatchRampNumbers>',
        '<ControlParameters>',
        '<ControlParameter>1</ControlParameter>',
        '</ControlParameters>',
        '</OrderData>',
        '</Host2KiSoft>',
    ]

    print_data = [
        '<Host2KiSoft messageID="150">',
        f'<PrintDataMessage orderNumber={orderNumber}>',
        '<DispatchRampNumbers>',
        '<DispatchRampNumber>114</DispatchRampNumber>',
        '</DispatchRampNumbers>',
        '<ControlParameters>',
        '<ControlParameter>9003</ControlParameter>',
        '</ControlParameters>',
        '<CheckCode>11110000642114410302</CheckCode>',
        '</PrintDataMessage>',
        '</Host2KiSoft>',   
    ]
    
    with open(filepath, "w") as f:
        f.write(f'Generated {orderAmount} orders with starting order number "{orderNumber}" and load unit code "{load_unit_code}"\r\n');
        for i in range(orderAmount):
            f.write("\n".join(order_data));
            f.write("\n");
            f.write("\n".join(print_data));
            f.write("\r\n");

    with open(filepath) as f:
        print(f.read());

write_dispatch_orders(filepath);