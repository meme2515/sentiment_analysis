test = {
  'name': 'q5e',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(trump.loc[744701872456536064, 'polarity'], 8.4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(trump.loc[745304731346702336, 'polarity'], 2.5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(trump.loc[744519497764184064, 'polarity'], 1.7)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(trump.loc[894661651760377856, 'polarity'], 0.2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(trump.loc[894620077634592769, 'polarity'], 5.4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # If you fail this test, you dropped tweets with 0 polarity;
          >>> np.allclose(trump.loc[744355251365511169, 'polarity'], 0.0)
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
