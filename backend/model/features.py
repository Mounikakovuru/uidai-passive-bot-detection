
# model/features.py

FEATURE_ORDER = [
    "num_plugins",
    "num_languages",
    "language_code",
    "timezone_offset",
    "screen_width",
    "screen_height",
    "pixel_depth",
    "device_memory",
    "hardware_concurrency",
    "cpu_class",
    "touch_support",
    "is_mobile",
    "cookie_enabled",
    "java_enabled",
]

def extract_features(data: dict) -> dict:
    # Safely extract language code
    language = data.get("language", {})
    if isinstance(language, dict):
        language_code = language.get("code", 0)
    else:
        language_code = language or 0

    # Safely extract timezone offset
    timezone = data.get("timezone", {})
    if isinstance(timezone, dict):
        timezone_offset = timezone.get("offset", 0)
    else:
        timezone_offset = timezone or 0

    # Get screen, device, browser sections safely
    screen = data.get("screen", {})
    if not isinstance(screen, dict):
        screen = {}

    device = data.get("device", {})
    if not isinstance(device, dict):
        device = {}

    browser = data.get("browser", {})
    if not isinstance(browser, dict):
        browser = {}

    features = {
        "num_plugins": len(data.get("plugins", [])) if isinstance(data.get("plugins", []), list) else 0,
        "num_languages": len(data.get("languages", [])) if isinstance(data.get("languages", []), list) else 0,
        "language_code": language_code,
        "timezone_offset": timezone_offset,
        "screen_width": screen.get("width", 0),
        "screen_height": screen.get("height", 0),
        "pixel_depth": screen.get("pixelDepth", 0),
        "device_memory": device.get("memory", 0),
        "hardware_concurrency": device.get("hardwareConcurrency", 0),
        "cpu_class": device.get("cpuClass", 0),
        "touch_support": int(device.get("touchSupport", False)),
        "is_mobile": int(device.get("isMobile", False)),
        "cookie_enabled": int(browser.get("cookieEnabled", False)),
        "java_enabled": int(browser.get("javaEnabled", False)),
    }

    return features

def features_dict_to_vector(features: dict) -> list:
    # Convert dict to list in FEATURE_ORDER, default 0 if missing
    return [features.get(feat, 0) for feat in FEATURE_ORDER]
