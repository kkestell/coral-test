"""A small double-entry ledger: accounts, postings, balances, and a trial balance."""

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Posting:
    account: str
    amount: Decimal


@dataclass(frozen=True)
class Entry:
    when: date
    memo: str
    postings: tuple[Posting, ...]

    def balanced(self) -> bool:
        return sum((posting.amount for posting in self.postings), Decimal(0)) == 0


@dataclass
class Ledger:
    accounts: set[str] = field(default_factory=set)
    entries: list[Entry] = field(default_factory=list)

    def open(self, account: str) -> None:
        if account in self.accounts:
            raise ValueError(f"{account} is already open")
        self.accounts.add(account)

    def post(self, when: date, memo: str, *postings: Posting) -> Entry:
        for posting in postings:
            if posting.account not in self.accounts:
                raise KeyError(posting.account)
        entry = Entry(when, memo, tuple(postings))
        if len(postings) < 2:
            raise ValueError("an entry needs at least two postings")
        self.entries.append(entry)
        return entry

    def balance(self, account: str, through: date | None = None) -> Decimal:
        total = Decimal(0)
        for entry in self.entries:
            if through is not None and entry.when >= through:
                continue
            for posting in entry.postings:
                if posting.account == account:
                    total += posting.amount
        return total

    def trial_balance(self) -> dict[str, Decimal]:
        return {account: self.balance(account) for account in sorted(self.accounts)}

    def close_period(self, through: date, equity: str) -> Entry:
        closing = []
        for account in self.accounts:
            if account.startswith("income:") or account.startswith("expense:"):
                amount = self.balance(account, through)
                if amount:
                    closing.append(Posting(account, -amount))
        total = sum((posting.amount for posting in closing), Decimal(0))
        closing.append(Posting(equity, total))
        return self.post(through, "close period", *closing)


def parse_amount(text: str) -> Decimal:
    """Parse "1,234.50", "(12.00)" for a negative, or "-3"."""
    text = text.strip().replace(",", "")
    if text.startswith("(") and text.endswith(")"):
        return -Decimal(text[1:-1])
    return Decimal(text)


def load(lines: list[str], ledger: Ledger) -> int:
    """Load entries written as `YYYY-MM-DD memo | account amount; account amount`."""
    count = 0
    for number, line in enumerate(lines, 1):
        if not line.strip() or line.startswith("#"):
            continue
        head, _, body = line.partition("|")
        day, _, memo = head.strip().partition(" ")
        postings = []
        for part in body.split(";"):
            account, amount = part.split()
            postings.append(Posting(account, parse_amount(amount)))
        ledger.post(date.fromisoformat(day), memo, *postings)
        count += 1
    return count
