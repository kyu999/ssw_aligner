# SSW Aligner

Python implementation of [Striped Smith-Waterman Algorithm](https://academic.oup.com/bioinformatics/article/23/2/156/205631)

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

※This repository uses a part of codes fetched from [scikit-bio](https://github.com/biocore/scikit-bio)
