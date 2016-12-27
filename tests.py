import lzss

tests = [
    {
        "message": "кибернетики",
        "buffer_size": 4,
        "dict_size": 12,
        "result": [
            (0, 'к'),
            (0, 'и'),
            (0, 'б'),
            (0, 'е'),
            (0, 'р'),
            (0, 'н'),
            (1, 3, 1),
            (0, 'т'),
            (1, 7, 1),
            (1, 9, 2)
        ]
    },
    {
        "message": "aababcabd",
        "buffer_size": 4,
        "dict_size": 12,
        "result": [
            (0, 'a'),
            (1, 1, 1),
            (0, 'b'),
            (1, 2, 2),
            (0, 'c'),
            (1, 3, 2),
            (0, 'd')
        ]
    }
]

for test in tests:
    result = lzss.compress(test['message'], test['buffer_size'], test['dict_size'])
    print(result)
    assert result == test['result']

    message = lzss.decompress(test['result'])
    print(message)
    assert message == test['message']
    print('===========================')