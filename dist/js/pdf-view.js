/** This code is under the Apache License Version 2.0, January 2004
 * http://www.apache.org/licenses/, as it is heavily based on
 * documentation of pdf.js (which is under Apache License v2.0)
 */

PDFJS.workerSrc = '/dist/js/pdf.worker.min.js';

var url = '/presentations/investors2017.pdf';

var pdfDoc = null,
    pageNum = 1,
    pageRendering = false,
    pageNumPending = null,
    scale = 1,
    canvasLeft = document.getElementById('the-canvas-left'),
    canvasRight = document.getElementById('the-canvas-right');

/**
 * Get page info from document, resize canvas accordingly, and render page.
 * @param num Page number.
 */
function renderPage(canvas,num) {
  pageRendering = true;
  // Using promise to fetch the page
  pdfDoc.getPage(num).then(function(page) {
    var viewport = page.getViewport(scale);
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    // Render PDF page into canvas context
    var renderContext = {
        canvasContext: canvas.getContext('2d'),
        viewport: viewport
    };
    var renderTask = page.render(renderContext);

    // Wait for rendering to finish
    renderTask.promise.then(function() {
      pageRendering = false;
      if (pageNumPending !== null) {
        // New page rendering is pending
        renderPage(pageNumPending);
        pageNumPending = null;
      }
    });
  });
}

/**
 * If another page rendering in progress, waits until the rendering is
 * finised. Otherwise, executes rendering immediately.
 */
function queueRenderPage(num) {
  if (pageRendering) {
    pageNumPending = num;
  } else {
    renderPage(canvasLeft,num);
    renderPage(canvasRight,num+1);
  }
}

/**
 * Displays previous page.
 */
function onPrevPage(event) {
  event.preventDefault();
  if (pageNum <= 1) {
    return;
  }
  pageNum--;
  queueRenderPage(pageNum);
}
document.getElementById('canvas-left').addEventListener('click', onPrevPage);

/**
 * Displays next page.
 */
function onNextPage(event) {
  event.preventDefault();
  if (pageNum >= pdfDoc.numPages - 1) {
    return;
  }
  pageNum++;
  queueRenderPage(pageNum);
}
document.getElementById('canvas-right').addEventListener('click', onNextPage);

document.getElementById('canvas-left').style.display = 'block';
document.getElementById('canvas-right').style.display = 'block';


function onMouseDown(event) {
  event.preventDefault();
}

document.getElementById('canvas-left').addEventListener('mousedown', onMouseDown);
document.getElementById('canvas-right').addEventListener('mousedown', onMouseDown);

/**
 * Asynchronously downloads PDF.
 */
PDFJS.getDocument(url).then(function(pdfDoc_) {
  pdfDoc = pdfDoc_;

  // Initial/first page rendering
  renderPage(canvasLeft,pageNum);
  renderPage(canvasRight,pageNum + 1);
});
