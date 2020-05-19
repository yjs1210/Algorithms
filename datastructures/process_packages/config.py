{
  "name": "2020-may",
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
    "control": "ip_capped_lr_high",
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
        "name": "ip_capped_lr_high",
        "buckets": "11-90"
      },
      {
        "name": "ip_exact_lr_high",
        "buckets": "90-95"
      },
      {
        "name": "lp_capped_lr_low",
        "buckets": "95-100"
      }
    ]
  }
}