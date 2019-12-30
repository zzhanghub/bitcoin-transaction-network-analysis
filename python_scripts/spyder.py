from blockchain import blockexplorer


def parse_block(block):
    trans_list = block.transactions
    trans_hash_list = []
    trans_inputs = []
    trans_outputs = []
    for trans in trans_list:
        trans_hash_list.append(trans.hash)
        trans_inputs.append(trans.inputs)
        trans_outputs.append(trans.outputs)
    return trans_hash_list, trans_inputs, trans_outputs

def parse_trans(inputs, outputs):
    inputs_addrs = []
    inputs_vals = []
    outputs_addrs = []
    outputs_vals = []
    for input in inputs:
        if 'address' in dir(input) and 'value' in dir(input):
            inputs_addrs.append(input.address)
            inputs_vals.append(input.value)
    for output in outputs:
        if 'address' in dir(output) and 'value' in dir(output):
            outputs_addrs.append(output.address)
            outputs_vals.append(output.value)
    return inputs_addrs, inputs_vals, outputs_addrs, outputs_vals

def save_trans(addr_in, addr_out, val, filename='data.csv'):
    val = str(val)
    addr_in = str(addr_in)
    addr_out = str(addr_out)
    with open(filename, 'a+') as f:
        f.write(addr_in + ',' + addr_out + ',' + val + '\n')

if __name__ == "__main__":
    blockID = '00000000000000000012afa0710628d1c504f1d40e1fc1b71c8cc66982547d0b'
    for k in range(50):
        Flag = False
        print(blockID)
        while(not Flag):
            try:
                block = blockexplorer.get_block(blockID)
                Flag = True
            except Exception as err:
                print(str(err))
        trans_hash, trans_inputs, trans_outputs = parse_block(block)
        for i in range(len(trans_hash)):
            # 0-th transaction is 12.5:
            if i == 0:
                pass
                #save_trans('None', trans_outputs[i][0].address, trans_outputs[i][0].value)
            else:
                inputs_addrs, inputs_vals, outputs_addrs, outputs_vals = parse_trans(trans_inputs[i], trans_outputs[i])
                inputs_sum = 0.0
                outputs_sum = 0.0
                for val in inputs_vals:
                    inputs_sum += float(val)
                for val in outputs_vals:
                    outputs_sum += float(val)
                for i, addr_in in enumerate(inputs_addrs):
                    for j, addr_out in enumerate(outputs_addrs):
                        val = float(inputs_vals[i]) / inputs_sum * outputs_vals[j]
                        if val == 0.0:
                            continue
                        save_trans(addr_in, addr_out, int(val), filename='data_block%d.csv'%(k+1))
        
        print('Parse %d block done.' % (k+1))
        blockID = block.previous_block
        
        
    print('Done.')