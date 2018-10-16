# SSW Aligner

### Dependencies
- [Numpy==1.12.0](http://www.numpy.org/)
- [Cython==0.28.3](https://cython.org/)

### Installation
```
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
```
### Reference
- [scikit-bio](https://github.com/biocore/scikit-bio)
