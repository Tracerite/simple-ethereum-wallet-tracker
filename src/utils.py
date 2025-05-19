def validate_address(address):
    # Basic validation
    return len(address) == 42 and address.startswith("0x")