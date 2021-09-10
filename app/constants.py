from model_utils import Choices

STATUS = Choices(
    ("SAVED", "SAVED"),
    ("PREPARED", "PREPARED"),
    ("APPLIED", "APPLIED"),
    ("INTERVIEWING", "INTERVIEWING"),
    ("NEGOTIATING", "NEGOTIATING"),
    ("EXPIRED", "EXPIRED"),
    ("ACCEPTED", "ACCEPTED"),
    ("DECLINED", "DECLINED"),
)