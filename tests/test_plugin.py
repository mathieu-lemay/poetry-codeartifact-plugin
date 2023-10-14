import pytest

from poetry_codeartifact_plugin.plugin import RE_CODEARTIFACT_NETLOC


@pytest.mark.parametrize(
    ("netloc", "expected"),
    [
        (
            "a-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            ("a", "123456789012"),
        ),
        (
            "abcde-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            ("abcde", "123456789012"),
        ),
        (
            "repo-with-dashes-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            ("repo-with-dashes", "123456789012"),
        ),
        (
            "-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            None,
        ),
        (
            "-aaa-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            None,
        ),
        (
            "UPPER-CASE-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            None,
        ),
        (
            "snake_case-123456789012.d.codeartifact.us-east-1.amazonaws.com",
            None,
        ),
        (
            "repo-without-owner.d.codeartifact.us-east-1.amazonaws.com",
            None,
        ),
        (
            "repo-without-d-123456789012.codeartifact.us-east-1.amazonaws.com",
            None,
        ),
        (
            "repo-without-codeartifact-123456789012.d.us-east-1.amazonaws.com",
            None,
        ),
        (
            "repo-without-region-123456789012.d.codeartifact.amazonaws.com",
            None,
        ),
        (
            "repo-bad-domain-123456789012.d.codeartifact.us-east-1.azure.microsoft.com",
            None,
        ),
    ],
)
def test_codeartifact_netloc_regex(
    netloc: str, expected: tuple[str, str] | None
) -> None:
    matches = RE_CODEARTIFACT_NETLOC.match(netloc)
    if matches:
        res = matches.groups()
    else:
        res = None

    assert res == expected
