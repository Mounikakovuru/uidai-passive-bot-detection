export function collectInteractions(): Promise<any> {
  return new Promise((resolve) => {
    let mouseMoves = 0;
    let maxScroll = 0;

    const mouseHandler = () => (mouseMoves += 1);
    const scrollHandler = () => {
      maxScroll = Math.max(
        maxScroll,
        window.scrollY || document.documentElement.scrollTop
      );
    };

    window.addEventListener("mousemove", mouseHandler);
    window.addEventListener("scroll", scrollHandler);

    setTimeout(() => {
      window.removeEventListener("mousemove", mouseHandler);
      window.removeEventListener("scroll", scrollHandler);
      resolve({
        mouseMovement: mouseMoves,
        scrollDepth: maxScroll,
      });
    }, 3000);
  });
}
