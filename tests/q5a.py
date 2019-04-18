test = {
  'name': 'q5a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(sent, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sent.shape
          (7517, 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(sent.index[5000:5005])
          ['paranoids', 'pardon', 'pardoned', 'pardoning', 'pardons']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(sent['polarity'].head(), [-1.5, -0.4, -1.5, -0.4, -0.7])
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
