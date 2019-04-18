test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datetime import datetime;
          >>> ELEC_DATE = datetime(2016, 11, 8);
          >>> INAUG_DATE = datetime(2017, 1, 20);
          >>> set(trump[(trump['time'] > ELEC_DATE) & (trump['time'] < INAUG_DATE) ]['source'].unique()) == set(['Twitter Ads',
          ...  'Twitter Web Client',
          ...  'Twitter for Android',
          ...  'Twitter for iPhone'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
