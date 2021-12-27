from typing import Union


class LoanApprover:
    def __init__(self, max_loan_amount: float, name: str):
        self.name = name
        self._max_loan_amount = max_loan_amount

    @property
    def next_handler(self) -> "LoanApprover":
        return self._next_handler

    def set_next(self, handler: "LoanApprover") -> None:
        self._next_handler = handler

    def handle(self, amount: float) -> Union["LoanApprover", None]:
        if amount <= self._max_loan_amount:
            return self

        if hasattr(self, "next_handler"):
            return self.next_handler.handle(amount)

        return None


class LoanApprovalChain:
    def __init__(self, handler: LoanApprover) -> None:
        self.handler = handler

    def approve(self, amount: float) -> Union[LoanApprover, None]:
        approved_handler = self.handler.handle(amount)
        return approved_handler

    def print_approval_tree(self, amount: float) -> None:
        handler = self.approve(amount)
        if handler:
            print(f"Amount (${amount}) approved by {handler.name}")
        else:
            print(f"Amount (${amount}) not approved")


if __name__ == "__main__":
    employee = LoanApprover(10, "Employee <= 10")
    manager = LoanApprover(20, "Manager <= 20")
    director = LoanApprover(30, "Director <= 30")
    manager.set_next(director)
    employee.set_next(manager)

    chain = LoanApprovalChain(employee)
    chain.print_approval_tree(10)
    chain.print_approval_tree(20)
    chain.print_approval_tree(30)
    chain.print_approval_tree(40)
