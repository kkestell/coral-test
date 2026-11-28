from datetime import date
from decimal import Decimal

from ledger import Ledger, Posting, load, parse_amount


def opened(*accounts: str) -> Ledger:
    ledger = Ledger()
    for account in accounts:
        ledger.open(account)
    return ledger


def test_balance_sums_postings() -> None:
    ledger = opened("assets:cash", "income:sales")
    ledger.post(date(2026, 1, 2), "sale", Posting("assets:cash", Decimal(10)), Posting("income:sales", Decimal(-10)))
    assert ledger.balance("assets:cash") == 10


def test_parse_amount_handles_parentheses() -> None:
    assert parse_amount("(12.00)") == Decimal("-12.00")
    assert parse_amount("1,234.50") == Decimal("1234.50")


def test_load_reads_entries() -> None:
    ledger = opened("assets:cash", "expense:rent")
    assert load(["2026-01-01 rent | expense:rent 500; assets:cash (500)"], ledger) == 1
