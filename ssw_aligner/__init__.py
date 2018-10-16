from ssw_wrapper import StripedSmithWaterman


def local_pairwise_align_ssw(query_sequence,
                             target_sequence,
                             gap_open_penalty=11,
                             gap_extend_penalty=1,
                             match_score=2,
                             mismatch_score=-3):
    ssw = StripedSmithWaterman(query_sequence,
                               gap_open_penalty=gap_open_penalty,
                               gap_extend_penalty=gap_extend_penalty,
                               match_score=match_score,
                               mismatch_score=mismatch_score)
    alignment = ssw(target_sequence)
    return alignment
