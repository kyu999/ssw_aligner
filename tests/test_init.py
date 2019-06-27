# -*- coding: utf-8 -*-


from nose.tools import eq_
import json
from ssw_aligner import local_pairwise_align_ssw


class TestInit():
    def setUp(self):
        pass

    def test_local_pairwise_align_ssw(self):
        query_sequence = 'AATTT'
        target_sequence = 'GGTTAC'
        alignments = local_pairwise_align_ssw(query_sequence, target_sequence)
        eq_(
            json.loads(alignments.__repr__().replace('\'', '\"')),
            {
                'cigar': '2M',
                'optimal_alignment_score': 4,
                'query_begin': 2,
                'query_end': 3,
                'query_sequence': 'AATTT',
                'suboptimal_alignment_score': 0,
                'target_begin': 2,
                'target_end_optimal': 3,
                'target_end_suboptimal': 0,
                'target_sequence': 'GGTTAC'
            }
        )

