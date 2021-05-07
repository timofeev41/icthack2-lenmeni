class DatabaseBase:
    """Abstract class"""
    pass

class DatabaseWorker(DatabaseBase):
    """Main database worker class"""
    def __init__(self) -> None:
        super().__init__()