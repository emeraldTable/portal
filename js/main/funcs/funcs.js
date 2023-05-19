function createIframe(src, width, height) {
  const iframe = document.createElement("iframe");
  iframe.src = src;
  iframe.width = width;
  iframe.height = height;
  document.body.appendChild(iframe);
}

