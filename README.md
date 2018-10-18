# SSW Aligner

Python implementation of [Striped Smith-Waterman Algorithm](https://academic.oup.com/bioinformatics/article/23/2/156/205631)

# Comparison as of 2018/10/18
|| ssw_aligner | [swalign]() | [scikit-bio](https://github.com/biocore/scikit-bio) |
|:---:|:---:|:---:|:---:|
| Python2 | ○ | ○ | ✗ |
| Python3 | ○ | ○ | ○ |
| benchmark | 1.049 seconds | over 30 minutes | 1.567 seconds |
| zipped package size | 108 KB | 9 KB | 8.6 MB |
| Installable to Google Dataflow | ○ | ○ | ✗ |

### Dependencies
- [numpy>=1.12.0](http://www.numpy.org/)
- [Cython>=0.28.3](https://cython.org/)

### Installation
```
# if you do not have numpy
pip install numpy==1.12.0

# if you do not have Cython
pip install Cython==0.28.3

pip install ssw_aligner
```

### Quick Start
```
from ssw_aligner import local_pairwise_align_ssw

query_seq = 'TTTTTAAAAA'
target_seq = 'GGGGTTTT'
alignment = local_pairwise_align_ssw(query_seq,
                                     target_seq,
                                     gap_open_penalty=11,
                                     gap_extend_penalty=1,
                                     match_score=2,
                                     mismatch_score=-3)

# get score
alignment.optimal_alignment_score

# get query start, end
alignment.query_begin
alignment.query_end

# get target start, end
alignment.target_begin
alignment.target_end_optimal

# get aligned sequence
alignment.aligned_query_sequence
alignment.aligned_target_sequence

# get cigar infomation
alignment.cigar

# check whether the index starts from 0 or not
alignment.is_zero_based()

# make the index start from n(0 or 1)
alignment.set_zero_based(0) # start from 0
alignment.set_zero_based(1) # start from 1
```

##### Benchmark script:
```
import random
import time

from skbio import DNA
import skbio
import swalign
import ssw_aligner


match = 2
mismatch = -1
scoring = swalign.NucleotideScoringMatrix(match, mismatch)
sw = swalign.LocalAlignment(scoring)

bases = ['A', 'T', 'C', 'G']
def generate_gene(length):
    return ''.join([random.choice(bases) for i in range(0, length)])


def benchmark(align_func):
    start = time.time()
    for i in range(0, 100):
        for seq_length in range(100, 2000, 500):
            seq1, seq2 = generate_gene(seq_length), generate_gene(seq_length)
            align_func(seq1, seq2)
    return time.time() - start


# input should be DNA type
def benchmark_skbio(align_func):
    start = time.time()
    for i in range(0, 100):
        for seq_length in range(100, 2000, 500):
            seq1, seq2 = generate_gene(seq_length), generate_gene(seq_length)
            align_func(DNA(seq1), DNA(seq2))
    return time.time() - start


print('ssw_aligner')
ssw_aligner_time = benchmark(ssw_aligner.local_pairwise_align_ssw)
print(ssw_aligner_time)

print('skbio')
skbio_time = benchmark_skbio(skbio.alignment.local_pairwise_align_ssw)
print(skbio_time)

print('swalign')
swalign_time = benchmark(sw.align)
print(swalign_time)

```

This benchmark script is executed by the environment below:
- MacBook Air (13-inch, Mid 2012)
- Processor: 2 GHz Intel Core i7
- Memory: 8GB

※This repository uses a part of codes fetched from [scikit-bio](https://github.com/biocore/scikit-bio)
