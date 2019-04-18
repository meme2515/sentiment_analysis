test = {
  'name': 'q1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(trump, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 10000 < trump.shape[0] < 11000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> trump.shape[1] >= 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 831846101179314177 in trump.index
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(col in trump.columns for col in ['time', 'source', 'text', 'retweet_count'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.sometrue([('Twitter for iPhone' in s) for s in trump['source'].unique()])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> trump['time'].dtype == np.dtype('<M8[ns]')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> trump['text'].dtype == np.dtype('O')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> trump['retweet_count'].dtype == np.dtype('int64')
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
