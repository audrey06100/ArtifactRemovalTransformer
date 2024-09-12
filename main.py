import utils
import os

if __name__ == '__main__':
    # parameter setting
    input_path = './sampledata/'
    input_name = 'sampledata.csv'
    sample_rate = 256 # input data sample rate
    modelname = 'ART' # or 'ICUNet', 'ICUNet++', 'ICUNet_attn', 'ART'
    output_path = './sampledata/'
    output_name = 'outputsample.csv'

    # read the mapping result
    mapping_name = './sampledata/sample_mappingresult.json'
    batch_num, mapping_result = utils.read_mapping_result(mapping_name)

    for i in range(batch_num):

        # step1: Data preprocessing
        preprocess_data, channel_num = utils.preprocessing(input_path+input_name, sample_rate, mapping_result[i])
        # step2: Signal reconstruction
        reconstructed_data = utils.reconstruct(modelname, preprocess_data, output_name, i)
        # step3: Data postprocessing
        utils.postprocessing(reconstructed_data, sample_rate, output_path+output_name, mapping_result[i], i, channel_num)
