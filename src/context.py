from contextvars import ContextVar

from .models import User

current_user_context: ContextVar[User] = ContextVar('current_user_context', default=None)

# Inside your middleware
# req_id.set(user)

# Inside other functions, even different files, you import that variable
# req_id.get()
