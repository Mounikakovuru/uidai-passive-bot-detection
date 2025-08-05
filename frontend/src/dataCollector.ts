export function collectData() {
  return {
    userAgent: navigator.userAgent,
    screen: {
      width: window.screen.width,
      height: window.screen.height,
    },
    language: navigator.language,
    hardwareConcurrency: navigator.hardwareConcurrency,
    doNotTrack: navigator.doNotTrack,
    touchSupport: navigator.maxTouchPoints,
    timezoneOffset: new Date().getTimezoneOffset(),
  };
}
