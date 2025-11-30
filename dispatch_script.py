import os, random, base64;

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

default_checkcode = """^XA
^FO0,20,2^A0N,200,200^FB812,1,1,C^FD\&^FS
^FO30,200^GB750,400,10,B,5^FS
^FO0,280,2^A0N,200,200^FB812,1,1,C^FDA#CWM\&^FS
^FO50,650,2^A0N,40,40^FB812,1,1,L^FDGONZ-210162^FS
^FO50,700,2^A0N,30,30^FB750,20,7,L^FD99995000\&^FS
^FO20,1250,2^A0N,30,30^FB812,1,1,L^FD09.10.25 14:34:44\&^FS
^FO0,1280^GB812,0,6^FS
^FO80,1370^BY4^BCN,200,Y,N^FD>511110000072114410302^FS
^XZ"""

def encode_checkcode():
    encoded_checkcode = base64.b64encode(b'^XA^FO0,20,2^A0N,200,200^FB812,1,1,C^FD\&^FS^FO30,200^GB750,400,10,B,5^FS^FO0,280,2^A0N,200,200^FB812,1,1,C^FDA#CWM\&^FS^FO50,650,2^A0N,40,40^FB812,1,1,L^FDGONZ-210162^FS^FO50,700,2^A0N,30,30^FB750,20,7,L^FD99995000\&^FS^FO20,1250,2^A0N,30,30^FB812,1,1,L^FD09.10.25 14:34:44\&^FS^FO0,1280^GB812,0,6^FS^FO80,1370^BY4^BCN,200,Y,N^FD>511110000072114410302^FS^XZ');

    encoded_checkcode = str(encoded_checkcode).replace("'", "").replace("b", "");
    print(encoded_checkcode);

# randomize checkcode
# change last 3 character randomly
# generate metadata
# insert both into printdata

starting_checkcode = "511110000072114410302";


print(starting_checkcode);
print(len(starting_checkcode));
random_five_digit_num = random.randrange(10**5);
    
print(random_five_digit_num);
split_checkcode_at = 16;
split_checkcode = starting_checkcode[:split_checkcode_at];
print(split_checkcode);
new_checkcode = split_checkcode + str(random_five_digit_num);
print(new_checkcode);
print(len(new_checkcode));
metadata_to_decode = """XlhBCl5GTzAsMjAsMl5BME4sMjAwLDIwMF5GQjgxMiwxLDEsQ15GRFwmXkZTCl5GTzMwLDIwMF5HQjc1MCw0MDAsMT
AsQiw1XkZTCl5GTzAsMjgwLDJeQTBOLDIwMCwyMDBeRkI4MTIsMSwxLENeRkRBI0NXTVwmXkZTCl5GTzUwLDY1MCwyXkEwTiw0MCw0MF5GQjgxMiwx
LDEsTF5GREdPTlotMjEwMTYyXkZTCl5GTzUwLDcwMCwyXkEwTiwzMCwzMF5GQjc1MCwyMCw3LExeRkQ5OTk5NTAwMFwmXkZTCl5GTzIwLDEyNTAsMl
5BME4sMzAsMzBeRkI4MTIsMSwxLExeRkQwOS4xMC4yNSAxNDozNDo0NFwmXkZTCl5GTzAsMTI4MF5HQjgxMiwwLDZeRlMKXkZPODAsMTM3MF5CWTRe
QkNOLDIwMCxZLE5eRkQ+NTExMTEwMDAwMDcyMTE0NDEwMzAyXkZTCl5YWg=="""

order_data_template = [
    '<Host2KiSoft messageID="151">',
    '<OrderData orderNumber={orderNumber} sheetNumber="1">',
    '<OrderType>15</OrderType>',
    '<LoadUnitCode>{load_unit_code}</LoadUnitCode>',
    '<DispatchRampNumbers>',
    '<DispatchRampNumber>{dispatch_ramp}</DispatchRampNumber>',
    '</DispatchRampNumbers>',
    '<ControlParameters>',
    '<ControlParameter>1</ControlParameter>',
    '</ControlParameters>',
    '</OrderData>',
    '</Host2KiSoft>',
]

print_data_template = [
    '<Host2KiSoft messageID="150">',
    '<PrintDataMessage orderNumber={orderNumber}>',
    '<DispatchRampNumbers>',
    '<DispatchRampNumber>{dispatch_ramp}</DispatchRampNumber>',
    '</DispatchRampNumbers>',
    '<ControlParameters>',
    '<ControlParameter>11</ControlParameter>',
    '</ControlParameters>',
    '<CheckCode>{checkcode}</CheckCode>',
    '<MetaData>metadata</MetaData>',
    '</PrintDataMessage>',
    '</Host2KiSoft>',   
]

generated_order_data = [];
generated_print_data = [];

while(os.path.exists(filepath)): 
    count += 1;
    file_parts = defualt_filepath.split(".");
    print(file_parts);
    print("count: ", count);
    if(count <= 9):
        filepath = file_parts[0] + "_0" + str(count) + "." + file_parts[1];
    else:
        filepath = file_parts[0] + "_" + str(count) + "." + file_parts[1];
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
starting_dispatch_ramp = 114;
seq_dispatch_ramp = starting_dispatch_ramp;


load_unit_code = starting_load_unit_code;

for i in range(orderAmount):
    # random_dispatch_ramp = random.randrange(114, 127);
    seq_dispatch_ramp += 1;

    print(starting_checkcode);
    random_five_digit_num = random.randrange(10**5);
    
    print(random_five_digit_num);
    split_checkcode_at = 16;
    split_checkcode = starting_checkcode[:split_checkcode_at];
    print(split_checkcode);
    new_checkcode = split_checkcode + str(random_five_digit_num);
    print(new_checkcode);

    if(i % 14 == 0):
        seq_dispatch_ramp = starting_dispatch_ramp;

    if(i > 9):
        orderNumber = startOrderNumber + "_" + str(i + 1);
    else:
        orderNumber = startOrderNumber + "_0" + str(i + 1);
    load_unit_code = starting_load_unit_code + i;

    # used if we want random dispatch ramp numbers 114-127, no error lane
    # new_order_data = [line.format(orderNumber = orderNumber, load_unit_code = load_unit_code, dispatch_ramp = random_dispatch_ramp)
    #             for line in order_data_template];
    # new_print_data = [line.format(orderNumber=orderNumber, dispatch_ramp = random_dispatch_ramp)
    #             for line in print_data_template];

    new_order_data = [line.format(orderNumber = orderNumber, load_unit_code = load_unit_code, dispatch_ramp = seq_dispatch_ramp)
                        for line in order_data_template];
    new_print_data = [line.format(orderNumber=orderNumber, dispatch_ramp = seq_dispatch_ramp, checkcode = new_checkcode)
                        for line in print_data_template];


    generated_order_data.append(new_order_data);
    generated_print_data.append(new_print_data); 

joined_order_data = zip(generated_order_data, generated_print_data);

def write_dispatch_orders(filepath, tuple):
    
    with open(filepath, "w") as f:
        f.write(f'Generated {orderAmount} orders with starting order number "{startOrderNumber}" and load unit code "{starting_load_unit_code}"\r\n');
        for order_list, print_list in tuple:
            order_block = "\n".join(order_list);
            print_block = "\n".join(print_list);
            f.write(order_block + "\n" + print_block + "\n");
            f.write("\n");

    with open(filepath) as f:
        print(f.read());

write_dispatch_orders(filepath, joined_order_data);

def print_tuple(tuple):
    ele_count = 0;
    for n in tuple:
        ele_count += 1;
        print(n);
        print("count: ", ele_count);