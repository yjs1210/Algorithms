
# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    from collections import defaultdict

    dp_map = []
    for i in range(len(first_sequence)+1):
        dp_map += [[0]*(len(second_sequence)+1)]

    for i in range(len(first_sequence)):
        for j in range(len(second_sequence)):
            if first_sequence[i] == second_sequence[j]:
                dp_map[i+1][j+1] = dp_map[i][j] + 1
            else:
                dp_map[i+1][j+1] = max(dp_map[i+1][j], dp_map[i][j+1])
    
    return dp_map[len(first_sequence)][len(second_sequence)]
    
                
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
{
  "name": "2020-testmay",
  "start_dt": "2020-05-21",
  "end_dt": "2020-06-15",
  "algorithms": {
    "control": "ensemble-slim",
    "tests": [
      {
        "name": "ensemble-slim",
        "buckets": "0-100"
      }
    ]
  },
  "rules": {
    "control": "lp_capped_lr_high",
    "tests": [
      {
        "name": "random",
        "buckets": "0-5"
      },
      {
        "name": "blacklist_90",
        "buckets": "5-8"
      },
      {
        "name": "blacklist_360",
        "buckets": "8-11"
      },
      {
        "name": "lp_capped_lr_low",
        "buckets": "11-90"
      },
      {
        "name": "ip_exact_lr_high",
        "buckets": "90-95"
      },
      {
        "name": "ip_capped_lr_high",
        "buckets": "95-100"
      }
    ]
  }
}