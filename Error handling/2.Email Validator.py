ALLOWED_DOMAINS = ['.com', '.bg', '.org', 'net']


class MustContainAtSymbol(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()
while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbol('Email must contain @')

    username, domain, *rest = email.split('@')

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if '.' + domain.split('.')[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
