from t3_cicd_cli.constant.default import DEFAULT_OVERRIDE_OPTION


def assemble_request(**kwargs):
    """
    Assemble the request parameters with any number of parameters.
    """

    payload = {}

    for key, value in kwargs.items():
        if value:
            if key == DEFAULT_OVERRIDE_OPTION and isinstance(value, str):
                override = dict(item.split("=") for item in value.split(","))
                payload[key] = override
            else:
                payload[key] = value

    return payload
