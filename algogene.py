import random
import eel
# from algogene import Sequence
from sequence import Sequence

eel.init('web')


@eel.expose
def generate(sequence_length, sequence_type):
    sequence = Sequence()
    sequence.generate_sequence(sequence_length, sequence_type)
    results = sequence.get_sequence_info().split('\n')
    info = sequence.get_sequence_info()
    response = [result.split(': ')[1] for result in results]
    return response, info
    # return sequence.get_sequence_info()


@eel.expose
def set_Sequence(data):
    sequence = Sequence()
    sequence.set_sequence(data['sequence_strand'],
                          data['sequence_type'], data['sequence_label'])
    return sequence.get_sequence_info()


@eel.expose
def set_output(data, params):
    sequence = Sequence()
    sequence.set_sequence(data['sequence_strand'],
                          data['sequence_type'], data['sequence_label'])
    if params == 'information':
        return sequence.get_sequence_info()
    elif params == 'frequency':
        return sequence.nucleotide_frequency()
    elif params == 'transcription':
        return sequence.transcription()
    elif params == 'complement':
        return sequence.reverse_complement()
    elif params == 'content':
        return sequence.gc_content()
    elif params == 'aminoacid':
        return sequence.translate_seq()
    elif params == 'proteins':
        return sequence.all_proteins_from_orfs()
    elif params == 'frames':
        return sequence.gen_reading_frames()
    else:
        return sequence.get_sequence_info()


try:
    eel.start('index.html', size=(500, 400), mode='default')
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
